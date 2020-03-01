from pytonik.Model import Model 
from pytonik.Functions.iteration import iteration
class Service(Model, iteration):

    def __getattr__(self, item):
        return item

    def __init__(self):
        return None

    def list(self, status=""):
        query = self.table('service').where('service_status', '=', status).select().get()
        return query.rowCount, query.result

    