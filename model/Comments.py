from pytonik.Model import Model 
from pytonik.Functions.count import count
class Comments(Model, count):

    def __getattr__(self, item):
        return item

    def __call__(self):
       
        return ""

    def __init__(self):
        
        return None

    def count(self, blog_id=0):
        query = self.table('comments').count('blog_id', 'views').where('blog_id', blog_id).select().get()
        
        if query.rowCount > 1:
            return self.digit(query.result[0]['views']) 
        else:
            return self.digit(0) 

  