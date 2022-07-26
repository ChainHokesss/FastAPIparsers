import uvicorn

from src.app import container_general
from src.routers.lamoda import router as health_router


container_general.app.include_router(health_router)

if __name__ == '__main__':
    uvicorn.run(
        'src.app:container_general.app',
        host=container_general.config.service.host,
        port=container_general.config.service.port,
        reload=container_general.config.service.reload,
    )
