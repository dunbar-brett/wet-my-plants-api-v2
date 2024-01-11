from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

from app.core.config import Settings
from app.db.session import engine
from app.db.models.base import Base
from app.routes import router as api_router


origins = [
    "http://127.0.0.1.tiangolo.com",
    "https://127.0.0.1.tiangolo.com",
    "http://127.0.0.1",
    "http://127.0.0.1:8080",
]

def create_tables():         
	Base.metadata.create_all(bind=engine)

def include_router(app):
    app.include_router(api_router)


# def configure_staticfiles(app):
#     app.mount("/static", StaticFiles(directory="static"), name="static")

def start_application():
    app = FastAPI(title=Settings.PROJECT_NAME,version=Settings.PROJECT_VERSION)
    create_tables()
    include_router(app)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app


app = start_application()

@app.get("/")
async def main():
    # html_content = """
    #     <html>
    #         <head>
    #         </head>
    #         <body>
    #             <a href="/docs">Viewtestssss Documentation</a>
    #         </body>
    #     </html>
    # """
    # return HTMLResponse(content=html_content, status_code=200)
    return {"message":"Hello fadfas"}
