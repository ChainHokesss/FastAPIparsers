from fastapi import APIRouter
from typing import List

from src.dto.product_dto import ProductDto, ProductDbDto
from src.app import container_controller, container_parser


router = APIRouter(
    tags=['Lamoda router'],
    prefix='/lamoda'
)


@router.post('/create')
def create_product(product: ProductDto) -> str:
    return container_controller.lamoda.create(product)


@router.get('/get/{_id}', response_model=ProductDbDto)
def get_product(_id: str) -> ProductDbDto:
    return container_controller.lamoda.get(_id)


@router.get('/get-list', response_model=List[ProductDbDto])
def get_product_list() -> List[ProductDbDto]:
    return container_controller.lamoda.get_list()


# @router.post('/test-kafka')
# def test_kafka_send(data: str):
#     container_parser.lamoda.send_task(data)
#     return "sd"
#
# @router.get('/test-kafka-get')
# def test_kafka_get():
#     consumer = container_parser.lamoda.get_task()
#     for msg in consumer:
#         print(msg)
#     return "js"


@router.get('/test-parser')
def test_parser():
    container_parser.lamoda.lamoda_parse()
    return "OK"
