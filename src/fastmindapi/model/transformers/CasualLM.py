
class AutoModel:
    def __init__(self, tokenizer, model):
        self.tokenizer = tokenizer
        self.model = model
        pass

    @classmethod
    def from_path(self, model_path: str):
        from transformers import AutoModelForCausalLM, AutoTokenizer
        return AutoModel(AutoTokenizer.from_pretrained(model_path),
                         AutoModelForCausalLM.from_pretrained(model_path, device_map="auto"))

    def generate(self, input_text: str):
        inputs = self.tokenizer(input_text, return_tensors="pt").to(self.model.device)
        outputs = self.model.generate(**inputs, max_new_tokens=12)
        output_text = self.tokenizer.batch_decode(outputs, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
        return output_text
    
    def generate_next_token(self):
        pass

    def chat(self):
        pass