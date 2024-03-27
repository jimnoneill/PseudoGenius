import os
import numpy as np
from transformers import AutoModelForSequenceClassification, TrainingArguments, Trainer
from datasets import load_metric
from transformers import AutoTokenizer
from .utils import tokenize_and_format, load_tokenizer



model_checkpoint = "zhihan1996/DNA_bert_6"  # You can choose a model suitable for your task
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
handle = model_checkpoint.split('/')[-1]
path = f"pseudo_genius"

# Check whether the specified path exists or not
isExist = os.path.exists(path)
if not isExist:
    # Create a new directory because it does not exist
    os.makedirs(path)

# Define the compute metrics function
def compute_metrics(eval_pred):
    logits, labels = eval_pred
    predictions = np.argmax(logits, axis=-1)
    precision = precision_metric.compute(predictions=predictions, references=labels, average="binary")
    recall = recall_metric.compute(predictions=predictions, references=labels, average="binary")
    f1 = f1_metric.compute(predictions=predictions, references=labels, average="binary")
    return {
        "precision": precision["precision"],
        "recall": recall["recall"],
        "f1": f1["f1"],
    }

# Initialize the model
model = AutoModelForSequenceClassification.from_pretrained(model_checkpoint, num_labels=2)

# Initialize the metrics
precision_metric = load_metric("precision")
recall_metric = load_metric("recall")
f1_metric = load_metric("f1")

def train_model(train_dataset, test_dataset):
    # Tokenize the dataset
    tokenized_train_dataset = train_dataset.map(tokenize_and_format, batched=True)
    tokenized_test_dataset = test_dataset.map(tokenize_and_format, batched=True)

    # Training arguments
    training_args = TrainingArguments(
        output_dir=path,
        evaluation_strategy="epoch",
        learning_rate=2e-5,
        per_device_train_batch_size=8,
        per_device_eval_batch_size=8,
        num_train_epochs=3,
        weight_decay=0.01,
    )

    # Initialize Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_train_dataset,
        eval_dataset=tokenized_test_dataset,
        compute_metrics=compute_metrics,
    )

    # Train the model
    trainer.train()
    trainer.save_model()
    # Save the tokenizer as well along with the model
    tokenizer.save_pretrained(path)
