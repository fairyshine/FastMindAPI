
class AutoModel:
    def __init__(self, tokenizer, model):
        self.tokenizer = tokenizer
        self.model = model
        pass

    def generate_next_token(self):
        pass

    @classmethod
    def from_path(model_path: str):
        from transformers import AutoModelForCausalLM, AutoTokenizer
        return AutoModel(AutoTokenizer.from_pretrained(model_path),
                         AutoModelForCausalLM.from_pretrained(model_path, device_map="auto"))
