from fastapi import APIRouter, Request

PREFIX = ""

def get_index_info(request: Request):
    return "The FastMindAPI is running successfully."

def get_available_models(request: Request):
    client = request.app.state.client
    return client.module["model"].available_models 

def get_loaded_models(request: Request):
    client = request.app.state.client
    return [model_name for model_name in client.module["model"].loaded_models]

def get_basic_router():
    router = APIRouter(prefix=PREFIX)

    router.add_api_route("/index", get_index_info, methods=["GET"])
    router.add_api_route("/available_models", get_available_models, methods=["GET"])
    router.add_api_route("/loaded_models", get_loaded_models, methods=["GET"])
    return router
