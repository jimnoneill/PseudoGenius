# PseudoGenius
Pseudo Genius is a ML transformers-based package for the binary classification of gene sequences from Mycobacterium species into 'pseudogenes'.

## Installation

Clone this repository and navigate into the package directory:

```bash
git clone https://github.com/yourusername/PseudoGenius.git
cd PseudoGenius
```
Install the package:

```bash
cd PseudoGenius
pip install .
```

Usage
To run the model with a list of DNA and protein strings:
```python
from pseudogenius.model import predict

# Replace this with your actual data
dna_protein_list = [
    "DNA_sequence\tProtein_sequence",
    # ...
]

predictions = predict(dna_protein_list)
print(predictions)
```
The model was trained on the Mycobacterium leprae genbank file ([here](https://www.ncbi.nlm.nih.gov/nuccore/CP029543.1?report=genbank)) and has shown consistent results on other mycobacterium species. It has not been tested on species with a lower GC content like E. coli.

Contributing
Contributions to PseudoGenius are welcome! Please refer to the contributing guidelines for more information.

License
This project is licensed under the MIT License - see the LICENSE file for details.


