def set_tf32_if_available() -> None:
    """
    Optional: enable CUDA TF32 for speed if you like; keep deterministic behavior otherwise.
    """
    try:
        import torch
        if torch.cuda.is_available():
            torch.backends.cuda.matmul.allow_tf32 = False
            torch.backends.cudnn.allow_tf32 = False
    except Exception:
        pass
