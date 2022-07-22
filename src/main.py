import uvicorn

from app import container_general


if __name__ == '__main__':
    uvicorn.run(
        container_general.app,
        host=container_general.config.service.host,
        port=container_general.config.service.port,
        reload=container_general.config.service.reload
    )
