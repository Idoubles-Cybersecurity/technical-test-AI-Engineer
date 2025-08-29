# Technical Test AI-Engineer

## System setup

- Python 3.10+ recommended.
- Create a virtualenv.
- Install dependencies
- pip install -r requirements.txt

## Model

As part of this exercise the basel/ATTACK-BERT https://huggingface.co/basel/ATTACK-BERT model from Huggingface will be utilized to apply embeddings.

## Objectives

Build a small Python program that:

1. Loads an ATTACK/BERT model to produce sentence/paragraph embeddings.
2. Embeds a free-form paragraph that describes a MITRE ATT&CK technique (TTP).
3. Embeds two specific TTP descriptions: T1566 and T1134.
4. Computes and reports similarity between the paragraph and each TTP.
5. Returns the best-matching TTP (basic text classification by similarity).

## Rules

- Internet use is allowed (e.g., model downloads, library docs).
- No AI assistants (ChatGPT, Copilot, etc.) allowed for help.
- Code must be clean, modular, and organized with classes and methods.
- Provide clear setup/run instructions and tests.
- Deterministic outputs.

## What we give you

- An input paragraph that needs to be classified.
- A TTP description along with its TTP number (see ``data.py``).
- A scaffolded Python project you can expand. Different files include incomplete functions with a ``# Todo`` flag.

## Input paragraph
The following paragraph needs to be classified as part of this exercise:
````
Emotet has continuously sent out spam emails in campaigns designed to infect users via phishing attacks. These phishing emails used various methods to lure victims into first opening them, and then downloading and executing .xls files, with macros used to download the Emotet dropper.
````

## Required output
A JSON in following format:

````
{
  "model_name": "basel/ATTACK-BERT",
  "paragraph_embedding_shape": [768],
  "similarities": {
    "T1566": 0.83,
    "T1134": 0.22
  },
  "predicted_ttp": "T1566"
}
````

## Constraints & Guidance
- Model: Use basel/ATTACK-BERT
- Embeddings: Use mean pooling over token embeddings to get a fixed-size vector.
- Similarity: Use cosine similarity.
- Structure: Follow the class design in the scaffold (you may extend it).
- Testing: Provide at least 1 unit test:
  - Similarity score is within [−1, 1] and higher for a clearly related text to T1566.
