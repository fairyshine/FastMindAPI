from pydantic import BaseModel
from fastapi import APIRouter, Request

PREFIX = "/model"

class QuickModel(BaseModel):
    model_name: str
    model_type: str
    model_path: str



def add_model_info(request: Request, item: QuickModel):
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
        
        return True
    except Exception as e:
        return "【Error】: "+str(e)


def get_model_router():
    router = APIRouter(prefix=PREFIX)

    router.add_api_route("/add_info", add_model_info, methods=["POST"])
    router.add_api_route("/load/{model_name}", load_model, methods=["GET"])
    return router
