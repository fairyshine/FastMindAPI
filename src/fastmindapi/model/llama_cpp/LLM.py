
class LLM:
    def __init__(self, model):
        self.model = model

    @classmethod
    def from_path(model_path: str):
        from llama_cpp import Llama
        return Llama(model_path, n_gpu_layers=-1)
    
