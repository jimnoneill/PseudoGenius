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
## Usage

### Using Pre-trained Model for Prediction

PseudoGenius provides an easy way to classify gene sequences using a pre-trained model hosted on Hugging Face. To use the model for making predictions:

```python
from pseudogenius.model import load_model, predict

# Load the pre-trained model from Hugging Face
tokenizer, model = load_model()

# List of DNA and protein sequences concatenated with tabs
dna_protein_list = [
    "DNA_sequence\tProtein_sequence",
    # ... add more sequences
]

# Get predictions
predictions = predict(model, tokenizer, dna_protein_list)
print(predictions)

```
Model Evaluation
The model was trained on a dataset with the following label distribution:

Training set: Normal: 1923, Pseudos: 722
Test set: Normal: 220, Pseudos: 74
The confusion matrix for the model's predictions on the test set is shown below:

Confusion Matrix
![pseudo_genius_confusion_matrix](https://github.com/jimnoneill/PseudoGenius/assets/26029174/30def8fe-f80f-4b37-8729-bd3656b8c2e6)


Training Your Own Model
If you wish to train your own model with custom data, PseudoGenius also includes the training code. Refer to the training script located at pseudogenius/training.py for details on how to train your model.

The model was trained on the Mycobacterium leprae genbank file ([here](https://www.ncbi.nlm.nih.gov/nuccore/CP029543.1?report=genbank)) and has shown consistent results on other mycobacterium species. It has not been tested on species with a lower GC content like E. coli.


Contributing
Contributions to PseudoGenius are welcome! Please refer to the contributing guidelines for more information.

License
This project is licensed under the MIT License - see the LICENSE file for details.


