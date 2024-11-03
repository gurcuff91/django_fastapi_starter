import uvicorn

from project import settings

if __name__ == "__main__":
    uvicorn.run("project.asgi:application", reload=settings.DEBUG)
