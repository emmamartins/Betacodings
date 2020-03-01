from pytonik.Model import Model 
from pytonik.Functions.iteration import iteration
class Testimonies(Model, iteration):

    def __getattr__(self, item):
        return item

    def __init__(self):
        return None

    def list(self, status="", limit = 100000):
        query = self.table('testimony').where('status', status).limit(int(limit)).select().get()
        return query.rowCount, query.result

