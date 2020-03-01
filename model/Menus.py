from pytonik.Model import Model 
from pytonik.Functions.iteration import iteration
from pytonik.Functions.url import url
class Menus(Model, iteration, url):

    def __getattr__(self, item):
        return item

    def __init__(self, *args, **kwargs):
        return None


    def menus_query(self, parent=0, status=1):
        query = self.table('menus a').where('a.menu_status', '=', str(status)).where('a.menu_parent', '=', int(parent)).fromTable('menu').outerJoin(self.raw("(SELECT menu_parent, COUNT(*) AS Count FROM ba_menus GROUP BY menu_parent) sub"), 'a.menu_id', 'sub.menu_parent ').select('a.menu_id', 'a.menu_name', 'a.menu_status', 'a.menu_link', 'sub.Count').get()
        return query.rowCount, query.result


    def menu(self, parent=0, status=1):
       
        content = """<ul class='navbar-nav ml-auto'>"""
                        
        for menu in  self.menus_query(parent, status)[1]:
            if menu['Count'] is not None and menu['Count'] > 0:
                result_1 = self.menus_query(menu["menu_id"], 1)
                if result_1[0] > 0:
                    content +="""<li class="nav-item dropdown "><a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" href="{menu_link}" >{name}</a>""".format(name=menu["menu_name"], menu_link=menu["menu_link"] if menu["menu_link"] is not None  else "#")

                    content += '<div class="dropdown-menu" aria-labelledby="navbarDropdown">'
               
                    for menu_1 in result_1[1]:
                        content += '<a class="dropdown-item" href="{link}">{name}</a>'.format(link=str(menu["menu_link"]).format(url=self.url())  if menu_1["menu_link"] is not None else "#",
                                                                            name=menu_1["menu_name"])
                        
                    content += ' </div>'
                else:
                   content += '<li class="nav-item"><a class="nav-link" href="{link}">{name}</a></li>'.format(link=str(menu["menu_link"]).format(url=self.url())  if menu["menu_link"] is not None  else "#",
                                                                       name=menu["menu_name"])
          
                content += '</li>'
            else:
                content += '<li class="nav-item"><a class="nav-link" href="{link}">{name}</a></li>'.format(link=str(menu["menu_link"]).format(url=self.url()) if menu["menu_link"] is not None else "#",
                                                                       name=menu["menu_name"])
        content +="""
                    <a href="{url}" id="hire__btn" class="hire__btn">Become Contributor</a></li>
                    
                    </ul>
                    """.format(url=self.url('contributor'))
        return content

    def all(self):
        query = self.table('menus').select().get()
        return query.rowCount, query.result 
    
