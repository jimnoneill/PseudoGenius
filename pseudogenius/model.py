import numpy as np
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

def load_model(model_name="jimnoneill/pseudogenius"):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    return tokenizer, model

# Function to make predictions using the pre-trained model
def predict(model, tokenizer, dna_protein_list):
    # Tokenize the input
    tokenized_input = tokenizer(dna_protein_list, padding="max_length", truncation=True, max_length=512, return_tensors="pt")

    # Generate predictions
    model.eval()
    with torch.no_grad():
        output = model(**tokenized_input)
    logits = output.logits
    predictions = np.argmax(logits, axis=-1)
    return predictions

# Users can now do the following in their code:
# from pseudogenius.model import load_model, predict
# tokenizer, model = load_model()
# predictions = predict(model, tokenizer, ["DNA_sequence\tProtein_sequence"])
