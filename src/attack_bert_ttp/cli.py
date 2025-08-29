import json
import argparse
from .embeddings import EmbeddingModel
from .classifier import TTPSimilarityClassifier


def parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description="ATTACK/BERT TTP similarity classifier")
    ap.add_argument("--paragraph", type=str, required=False, help="Free text paragraph to classify")
    return ap.parse_args()


def main() -> None:
    args = parse_args()
    paragraph = args.paragraph

    if not paragraph:
        raise SystemExit("Provide --paragraph")

    embedder = EmbeddingModel()  # Todo
    clf = TTPSimilarityClassifier(embedder)

    pred, sims = clf.predict(paragraph)
    result = {
        "model_name": "basel/ATTACK-BERT",
        "paragraph_embedding_shape": "TODO",  # fill with actual vector shape
        "similarities": sims,
        "predicted_ttp": pred
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
