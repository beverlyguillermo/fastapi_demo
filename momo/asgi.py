from .main import get_app
from .books.endpoints import router
from . import __version__


app = get_app()
app.include_router(router)

@app.get("/")
async def root():
    return { "version": __version__ }
