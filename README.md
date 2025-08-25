Setup

Python 3.10+ recommended.

Create a virtualenv.

Install dependencies (choose one):

pip install -r requirements.txt
or

pip install -e . (if using pyproject.toml)

If you cannot find a package literally named “ATTACK/BERT”, select a close BERT-based sentence embedding model from Hugging Face and set:

export ATTACK_BERT_MODEL=<model-id>