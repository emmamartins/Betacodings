from pytonik.Model import Model 
from pytonik.Functions.iteration import iteration
from pytonik.Functions.url import url
from pytonik.Functions.path import path
from pytonik.App import App 
class Blog(Model, iteration, url, App):

    def __getattr__(self, item):
        return item

    def __call__(self):
        return ""

    def __init__(self):
        self.path  = path()
        return None

    def status(self, status="", code=""):
        query = ""
        if code is not "":
    
            query = self.table('blog').where('blog_status', '=', status).where('blog_lang', '=', code).select().get()
        
        elif status is not "":
            query = self.table('blog').where('blog_status', '=', status).select().get()

        else:
            query = self.table('blog').select().get()
        return query.rowCount, query.result

    def list(self, status, offset, limit, code=""):
        query = ""
        
        if code is not "":

            query = self.table('blog').where('blog_status', '=', status).where('blog_lang', '=', code).offset(offset).limit(limit).orderBy('blog_id', 'DESC').select().get()
        
        elif status is not "":
            query = self.table('blog').where('blog_status', '=', status).offset(offset).limit(limit).orderBy('blog_id', 'DESC').select().get()
       
        else:
            query = self.table('blog').offset(offset).limit(limit).orderBy('blog_id', 'DESC').select().get()
        
        return query.rowCount, query.result

     
    def id(self, id=""):
        query = self.table('blog').where('blog_id', '=', id).select().get()
        return query.rowCount, query.result
    
    def para(self, para="", status=""):
        query = self.table('blog').where('blog_para', '=', para).select().get()
        return query.rowCount, query.result

    def notin(self, status):
        query = self.table('blog').where('blog_status', status).select().get()
        return query.rowCount, query.result

    def keywords(self, id = ""):
        if id is "":
            query = self.table("blog").select().get()
        else:
            query = self.table("blog").where('blog_id', '!=', id).select().get()
        
        if query.rowCount > 0:
            keywords = [] 
            for result in query.result:
                keyword = result["blog_tag"]
                keywords.append(keyword)
            kw = []
            for k in self.keyword(keywords, 8):
                 ks= '<a id="tag" href="{url}"> <i class="fa fa-tags"></i> {k}</a>'.format(k=k, url="")
                 kw.append(ks)
            return " ".join(kw)
        else:
            return ""

    def recent(self, id = ""):
        
        if id is "":
            query = self.table("blog").orderBy('RAND()').limit(5).select().get()
        else:
            query = self.table("blog").where('blog_id', '!=', id).orderBy('RAND()').select().get()
        
        if query.rowCount > 0:
    			
            ks = """
                <div class="spanel " style="width: 100%;">
                <h3 class="text-center" >Recent Post</h3>

                <div class="feat__container__body">

                """
            for k in query.result:
                
                ks += """<div class="feat__contents">
                            <span class="feat__thumbs">

                            <img src="{img}" class="img-responsive" style="display: inline;">                           
                            </span>
                            <div class="feat__article">
                            <a href="{url}/read/{blog_para}">{blog_title}</a>  <br> 
                            <a href="{url}/blog/{lang}" style="font-weight: 700; color: #efbb5a;">
                            <i class="devicon-{lang}-plain colored"></i> {lang}</a>
                            </div>
                            </div>""".format(img = self.path.exist("public/uploads/img/180x180_"+k["blog_img"], "/assets/img/web-design-nigeria-2-e1482857749578.jpg")  if k["blog_img"] is "" else k["blog_img"] , lang=k["blog_lang"], blog_para=k['blog_para'],  url=self.url(), blog_title=k['blog_title'])
            ks += """</div></div>"""
            return ks
        else:
	        return ""
            
    def codes(self, status=""):
        query = self.table('lang').where('lang_status', '=', status).select().get()
        return query.rowCount, query.result
    
    def insert(self, data):
        
        query = self.table('blog').insert(data)
        return query
    
    def update(self, id, data):

        query = self.table('blog').where('blog_id', '=', id).update(data)
        return query
    
    