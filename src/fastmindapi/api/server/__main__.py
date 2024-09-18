from . import app

class Client:
    def __init__(self):
        self.app = app
        self.port = 8000
        self.deploy_mode = "uvicorn"
        self.local_mode = False

        self.module["model"] 

    def run(self):
        match self.deploy_mode:
            case "uvicorn":
                import uvicorn
                uvicorn.run(self.app, 
                            host='0.0.0.0' if not self.local_mode else "127.0.0.1", 
                            port=self.port)
                
    