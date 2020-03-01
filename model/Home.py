from pytonik.Model import Model 
from pytonik.Functions.iteration import iteration
class Home(Model, iteration):

    def __getattr__(self, item):
        return item

    def __init__(self):
        return None

    def blog(self, status=""):
        query = self.table('blog').where('blog_status', '=', status).select().get()
        return query.rowCount, query.result

    