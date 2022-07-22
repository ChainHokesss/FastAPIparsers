import uvicorn

from app import container_general
# from


if __name__ == '__main__':
    uvicorn.run(
        container_general.app,

    )