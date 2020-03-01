from pytonik.Model import Model 
from pytonik.Functions.iteration import iteration
class Admin(Model, iteration):

    def __getattr__(self, item):
        return item

    def __init__(self):
        return None

    def list(self, status="", limit = 100000):
        query = self.table('admin').where('status', status).limit(int(limit)).select().get()
        return query.rowCount, query.result

    def id(self, id=0, column=""):
        query = self.table('admin').where('admin_id', int(id)).select().get()
        
        if query.rowCount > 0:
            if column is "":
                return query.result[0]
            else:
                return query.result[0]["admin_fullname"]

    
