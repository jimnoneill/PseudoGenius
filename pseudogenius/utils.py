import pandas as pd
from Bio import SeqIO
from transformers import AutoTokenizer

# Process GenBank file to extract gene information
def process_genes(gbk_file):
    genes = {
        'normal_genes': [],
        'pseudo_frameshift': [],
        'pseudo_incomplete': [],
        'pseudo_stop': [],
        'pseudo_multi': [],
        'pseudos': []
    }

    for record in SeqIO.parse(gbk_file, "genbank"):
        for feature in record.features:
            if feature.type == 'CDS':
                if 'pseudo' not in feature.qualifiers:
                    genes['normal_genes'].append(NormalGene(feature, record.seq))
                else:
                    note = feature.qualifiers.get('note', [''])[0]
                    if 'frame' in note:
                        genes['pseudo_frameshift'].append(PseudoFrameShift(feature, record.seq))
                    elif 'inc' in note:
                        genes['pseudo_incomplete'].append(PseudoIncomplete(feature, record.seq))
                    elif 'stop' in note:
                        genes['pseudo_stop'].append(PseudoStop(feature, record.seq))
                    if any(term in note for term in ['frame', 'inc', 'stop']):
                        genes['pseudo_multi'].append(PseudoMulti(feature, record.seq))
                    genes['pseudos'].append(Pseudos(feature, record.seq))
    return genes

# Create a dataset for training from gene information
def create_dataset(genes):
    data = []
    for gene in genes['normal_genes']:
        sequence = str(gene.sequence)
        amino_acids = gene.amino_acids
        data.append({'text': sequence + "\t" + amino_acids, 'label': 0})
    for gene in genes['pseudos']:
        sequence = str(gene.sequence)
        amino_acids = gene.amino_acids
        data.append({'text': sequence + "\t" + amino_acids, 'label': 1})
    return pd.DataFrame(data)

# Function to tokenize sequences for the model
def tokenize_function(examples, tokenizer):
    return tokenizer(examples["text"], padding="max_length", truncation=True, max_length=512)

# Load a tokenizer from a model checkpoint
def load_tokenizer(checkpoint="zhihan1996/DNA_bert_6"):
    return AutoTokenizer.from_pretrained(checkpoint)
