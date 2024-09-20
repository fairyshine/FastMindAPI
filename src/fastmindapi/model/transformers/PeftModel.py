from .CasualLM import TransformersCausalLM

class PeftCausalLM(TransformersCausalLM):
    def __init__(self, base_model: TransformersCausalLM, peft_model):
        self.raw_model = base_model.model
        self.tokenizer = base_model.tokenizer
        self.model = peft_model
        pass

    @classmethod
    def from_path(self, base_model: TransformersCausalLM, model_path: str):
        from peft import PeftModelForCausalLM
        return PeftCausalLM(base_model,
                            PeftModelForCausalLM.from_pretrained(base_model.model,model_path))
