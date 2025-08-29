from typing import List
import torch
import numpy as np

class EmbeddingModel:
    """
    Loads a BERT-like model (preferably ATTACK/BERT) and produces sentence/paragraph embeddings.
    Implement: __init__, encode, _mean_pool, _setup_seed
    """
    def __init__(self, model_name: str, max_length: int = 384, seed: int = 42):
        self.model_name = model_name
        self.max_length = max_length
        self._setup_seed(seed)
        # TODO: load tokenizer + model; consider sentence-transformers if chosen
        # self.tokenizer = ...
        # self.model = ...
        # self.model.to(self.device).eval()

    def _setup_seed(self, seed: int) -> None:
        torch.manual_seed(seed)
        np.random.seed(seed)

    def _mean_pool(self, model_outputs, attention_mask: torch.Tensor) -> torch.Tensor:
        """
        Implement standard mean pooling over token embeddings (last hidden state).
        """
        # TODO: implement pooling
        raise NotImplementedError

    @torch.inference_mode()
    def encode(self, texts: List[str]) -> np.ndarray:
        """
        Returns a 2D numpy array (n_texts, hidden_size).
        """
        # TODO: tokenize, run model, pool, return np.ndarray on CPU
        raise NotImplementedError
