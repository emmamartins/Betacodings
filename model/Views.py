from pytonik.Model import Model 
from pytonik.Functions.count import count
class Views(Model, count):

    def __getattr__(self, item):
        return item

    def __call__(self):
        
        return ""

    def __init__(self):
        
        return None

    def count(self, blog_id=0):
        query = self.table('views').count('blog_id', 'views').where('blog_id', blog_id).select().get()
        if query.rowCount > 0:
            return self.digit(query.result[0]['views']) 
        else:
            return  '0'

    def list(self, ip, blog_id=0):
        query = self.table('views').where('blogviews_ip', ip).where('blog_id', blog_id).select().get()
        return query.rowCount, query.result
        
    def insert(self, data):
        query = self.table('views').insert(data)
        return query
        