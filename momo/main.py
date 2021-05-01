from fastapi import FastAPI

def get_app():
    app = FastAPI(title="FastApi Demo")
    return app
