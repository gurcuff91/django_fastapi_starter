from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def index():
    return {"app": "django_fastapi_starter"}


@router.get("/healthcheck")
def health_check():
    return {"status": "ok"}
