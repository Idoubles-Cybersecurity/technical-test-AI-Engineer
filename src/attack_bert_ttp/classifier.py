from typing import Dict, Tuple
import numpy as np
from .embeddings import EmbeddingModel
from .data import builtin_ttps

class TTPSimilarityClassifier:
    """
    Encodes a free-text paragraph and compares to known TTP embeddings via cosine similarity.
    """
    def __init__(self, embedder: EmbeddingModel):
        self.embedder = embedder
        self.ttps = builtin_ttps()
        self._ttp_matrix = None
        self._order = None

    def _build_ttp_matrix(self) -> None:
        if self._ttp_matrix is not None:
            return
        texts = [entry.text for entry in self.ttps.values()]
        self._order = list(self.ttps.keys())
        self._ttp_matrix = self.embedder.encode(texts)  # shape: (k, d)

    def score(self, paragraph: str) -> Dict[str, float]:
        """
        Returns a dict of {ttp_id: similarity}.
        """
        self._build_ttp_matrix()
        p_vec = self.embedder.encode([paragraph])[0]  # (d,)
        sims = {}
        for i, ttp_id in enumerate(self._order):
            t_vec = self._ttp_matrix[i]
            # TODO: compute cosine similarity
            raise NotImplementedError
        return sims

    def predict(self, paragraph: str) -> Tuple[str, Dict[str, float]]:
        sims = self.score(paragraph)
        best = max(sims.items(), key=lambda kv: kv[1])[0]
        return best, sims
