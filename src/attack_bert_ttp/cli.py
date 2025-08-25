import json
import os
import argparse
from .config import ModelConfig
from .embeddings import EmbeddingModel
from .classifier import TTPSimilarityClassifier

def parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description="ATTACK/BERT TTP similarity classifier")
    ap.add_argument("--model-name", type=str, default=os.getenv("ATTACK_BERT_MODEL", "ATTACK/BERT"))
    ap.add_argument("--device", type=str, default=os.getenv("DEVICE"))
    ap.add_argument("--max-length", type=int, default=384)
    ap.add_argument("--paragraph", type=str, required=False, help="Free text paragraph to classify")
    ap.add_argument("--paragraph-file", type=str, help="Path to a text file with paragraph")
    return ap.parse_args()

def main() -> None:
    args = parse_args()
    paragraph = args.paragraph
    if args.paragraph_file:
        with open(args.paragraph_file, "r", encoding="utf-8") as f:
            paragraph = f.read().strip()
    if not paragraph:
        raise SystemExit("Provide --paragraph or --paragraph-file")

    cfg = ModelConfig(model_name=args.model_name, device=args.device, max_length=args.max_length)
    embedder = EmbeddingModel(cfg.model_name, cfg.device, cfg.max_length, cfg.seed)
    clf = TTPSimilarityClassifier(embedder)

    pred, sims = clf.predict(paragraph)
    result = {
        "model_name": cfg.model_name,
        "paragraph_embedding_shape": "TODO",  # fill with actual vector shape
        "similarities": sims,
        "predicted_ttp": pred
    }
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
