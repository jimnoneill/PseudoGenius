from Bio import SeqIO

class Gene:
    def __init__(self, feature, parent_sequence):
        self.feature = feature
        self.locus_tag = feature.qualifiers.get('locus_tag', [''])[0]
        self.sequence = feature.location.extract(parent_sequence)
        self.amino_acids = feature.qualifiers.get('translation', [''])[0]

# Derived class for normal genes
class NormalGene(Gene):
    pass

# Derived class for different categories of pseudogenes
class PseudoFrameShift(Gene):
    pass

class PseudoIncomplete(Gene):
    pass

class PseudoStop(Gene):
    pass

class PseudoMulti(Gene):
    pass

class Pseudos(Gene):
    pass

# Function to process genes from a genbank file
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
                    if ('frame' and 'inc') or ('stop' and 'frame') or ('inc' and 'frame') or ('inc' and 'stop') in note:
                        genes['pseudo_multi'].append(PseudoMulti(feature, record.seq))
                    genes['pseudos'].append(Pseudos(feature, record.seq))

    return genes
