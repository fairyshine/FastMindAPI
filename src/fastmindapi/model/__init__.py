from .transformers.CasualLM import AutoModel as TransformersCausalLM

class ModelModule:
    def __init__(self):
        self.avaliable_models = dict()
        self.loaded_models = dict()

    def load_model(self, model_name: str, model_type: str=None, model_path: str=None):
        '''
        Load the specific model.
        '''
        # 更新模组的模型信息
        if model_name not in self.avaliable_models:
            self.avaliable_models[model_name] = dict()
        
        # 匹配模型类型
        match model_type:
            case "TransformersCasualLM":
                self.loaded_models[model_name] = TransformersCausalLM(model_path)

