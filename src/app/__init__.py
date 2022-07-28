from src.app.general import ContainerGeneral
from src.app.container_dao import ContainerDao
from src.app.container_controller import ContainerController
from src.app.container_parser import ContainerParser

container_general = ContainerGeneral()
container_dao = ContainerDao(container_general)
container_controller = ContainerController(db=container_dao.db)
container_parser = ContainerParser(container_general.config, container_controller)
