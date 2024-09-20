from pydantic import BaseModel, ConfigDict
from fastapi import APIRouter, Request

PREFIX = "/model"

class BasicModel(BaseModel):
    model_name: str
    model_type: str
    model_path: str
    model_foundation: str = None # for Peft Model
    model_config = ConfigDict(protected_namespaces=())

class GenerationRequest(BaseModel):
    model_name: str
    prompt: str
    max_new_tokens: int = None

    model_config=ConfigDict(protected_namespaces=())

def add_model_info(request: Request, item: BasicModel):
    client = request.app.state.client
    if item.model_name in client.module["model"].available_models:
        client.logger.info(item.model_name+" is already listed in [available_models].")
        if client.module["model"].available_models[item.model_name]["model_type"] != item.model_type:
            client.logger.info("Updating model type: "+client.module["model"].available_models[item.model_name]["model_type"]+" -> "+item.model_type+".")
            client.module["model"].available_models[item.model_name]["model_type"] = item.model_type
        if client.module["model"].available_models[item.model_name]["model_path"] != item.model_path:
            client.logger.info("Updating model path: "+client.module["model"].available_models[item.model_name]["model_path"]+" -> "+item.model_path+".")
            client.module["model"].available_models[item.model_name]["model_path"] = item.model_path
    else:
        client.module["model"].available_models[item.model_name] = {
            "model_type": item.model_type,
            "model_path": item.model_path
            }
    return True

def load_model(request: Request, model_name: str):
    client = request.app.state.client
    try:
        client.module["model"].load_model_from_path(model_name)
        return True
    except Exception as e:
        return "【Error】: "+str(e)
    
def unload_model(request: Request, model_name: str):
    client = request.app.state.client
    if model_name in client.module["model"].loaded_models:
        del client.module["model"].loaded_models[model_name]
        return model_name+" is released successfully."
    else:
        return model_name+" is not loaded right now."

def simple_generate(request: Request, item: GenerationRequest):
    client = request.app.state.client
    output_text = client.module["model"].loaded_models[item.model_name](input_text=item.prompt, 
                                                                        max_new_tokens=item.max_new_tokens if item.max_new_tokens!=None else None)
    return output_text


def get_model_router():
    router = APIRouter(prefix=PREFIX)

    router.add_api_route("/add_info", add_model_info, methods=["POST"])
    router.add_api_route("/load/{model_name}", load_model, methods=["GET"])
    router.add_api_route("/unload/{model_name}", unload_model, methods=["GET"])
    router.add_api_route("/call", simple_generate, methods=["POST"])
    return router
