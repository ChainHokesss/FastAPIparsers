from bson.objectid import ObjectId


class LamodaController:
    def __init__(self, db):
        self._db = db
        self._collection = db.lamoda

    @property
    def collection(self):
        return self._collection

    def create(self, product=None, data: dict = None) -> str:
        product_data = {}
        if data:
            product_data = data
        if product:
            product_data = product.dict()

        return str(self.collection.insert_one(product_data).inserted_id)

    def get(self, _id: str):
        data = self.collection.find_one({'_id': ObjectId(_id)})
        data['_id'] = str(data['_id'])
        return data

    def get_list(self):
        data_list = []

        for data in self.collection.find():
            data['_id'] = str(data['_id'])
            data_list.append(data)

        return data_list
