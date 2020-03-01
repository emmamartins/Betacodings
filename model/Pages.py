from pytonik.Model import Model 
from pytonik.Functions.iteration import iteration
class Pages(Model, iteration):

    def __getattr__(self, item):
        return item

    def __init__(self):
        return None

    def get(self, para, status=""):
        query = self.table('page').where('para', para).where('status', '=', status).select().get()
        return query.rowCount, query.result

    