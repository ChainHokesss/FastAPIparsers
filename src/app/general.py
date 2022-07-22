from fastapi import FastAPI


class ContainerGeneral:
    def __init__(self):
        self.__app = None

    @property
    def app(self):
        return FastAPI(
            title="FastAPIparsers"
        )