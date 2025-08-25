from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class ModelConfig:
    model_name: str = "ATTACK/BERT"  # override via env or CLI
    device: Optional[str] = None     # "cuda", "mps", or "cpu"
    max_length: int = 384
    batch_size: int = 8
    seed: int = 42
