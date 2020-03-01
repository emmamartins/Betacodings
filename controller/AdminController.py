from pytonik import Web
from pytonik.Functions.path import path


m = Web.App()
Helper = Web.Helpers()
file = Web.File()
pagination = Web.Pagination()
Blogs = Web.Load('Blog')

def index():
    data = {
        'title': "Beta Codings",
    }
    m.views('admin/index', data)


def login():
    data = {
        'title': "Beta Codings",
    }
    m.views('admin/login', data)


def blog(Request):
    #m.header()
    if Request.method == "GET":
        p = Request.params('page')
        if p is not "":
            para = int(p)
        else:
            para = 1

    num_per_page = 9

    start = 1 if (para - 1) < 1 else (para - 1)

    start_page = start * num_per_page

    listBlog = Blogs.list('', start_page, num_per_page)
    blog = Blogs.status()
    total = int(float(blog[0] + (num_per_page - 1)) / float(num_per_page))


    data = {
        'title': "Blog - Beta Codings",
        'listBlog': Helper.iteration(listBlog[1], 'xid'),
        'countBlog': listBlog[0],
        'paging': pagination.number(total=total, page=para, url='/admin/blog/page', css=['pagination justify-content-center mb-1', 'page-item',
                                                                              'page-link'])


    }
    m.views('admin/blog', data)


def addblog(Request):
    
    msg = ""
    
    if Request.method == "POST":
        
        pagename = Request.post('titlepage', 1)
        pagecontent = Request.post('ckeditor')
        feature_image = Request.file('feature_image')
        covertitl = Helper.alphanumeric(pagename)
        status = Request.post('status')
        newfile_name = ""
        pagepara = str(covertitl.replace(" ", "-")).lower()
        
        if pagename == "":
            msg = " <div class='alert alert-danger material_alert material_alert_danger' > <button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>x</span></button>  Enter Page Name</div>"
        elif pagecontent == "":
            msg = " <div class='alert alert-danger material_alert material_alert_danger' > <button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>x</span></button>  Enter Page Content </div>"

        else:
           
            if feature_image is not "":

                upload_dir = Helper.mvc_dir('public/uploads/img/blog')

                listext = ['png', 'jpg', 'JPG', 'jpeg']
                dimension = {550: 446, 770: 450, 120: 80}
                size = 1024 * 1024 * 2  # 2MB File Size Allowed Only
                ext = file.ext(feature_image.filename)

                upload = file.Image(upload_dir, feature_image)

                
                rename = str(pagepara) + str(Helper.rand(6))
                

                newfile_name = rename + upload.filename
                

                if ext in listext:
                    if size >= upload.size():

                        for w, h in dimension.items():
                            upload.resize(w, h, rename)
                            
                        # update profile image
                        respons_img = file.upload(feature_image, upload_dir, rename)
                        

                    else:
                        msg = " <div class='alert alert-danger material_alert material_alert_danger' > <button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>x</span></button>  Enter Page Content </div>"
                else:
                    msg = " <div class='alert alert-danger material_alert material_alert_danger' > <button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>x</span></button>  invalid Image File </div>"
            else:
                msg = ""
            info = [{
                "blog_para": pagepara,
                "blog_title": pagename,
                "blog_content": pagecontent,
                "blog_img": newfile_name,
                "admin_id": 1,
                "blog_status": 'PENDING' if status == "" else "APPROVED",
                "blog_createddate": Web.Functions().datetime(),
            }]
            response = Blogs.insert(info)
            

            if response is True:
                m.redirect(Web.url('/admin/blog/'))
                m.header()
            else:
                msg = " <div class='alert alert-danger ' > <button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>x</span></button>  Unable to process this action, try again later </div>"

    data = {
        'title': "Beta Codings",
        'msg': msg,
    }
    m.views('admin/addblog', data)




def updateblog(Request):
    #m.header()
    msg = ""
    id = ""
    if Request.method == "GET":
        id = Request.params('id')
    
    if Request.method == "POST":
        id = Request.post('id')
        pagename = Request.post('titlepage', 1)
        pagecontent = Request.post('ckeditor')
        feature_image = Request.file('feature_image')
        covertitl = Helper.alphanumeric(pagename)
        status = Request.post('status')
        newfile_name = ""
        pagepara = str(covertitl.replace(" ", "-")).lower()
        
        if pagename == "":
            msg = " <div class='alert alert-danger material_alert material_alert_danger' > <button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>x</span></button>  Enter Page Name</div>"
        elif pagecontent == "":
            msg = " <div class='alert alert-danger material_alert material_alert_danger' > <button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>x</span></button>  Enter Page Content </div>"

        else:
           
            if feature_image is not "":
                upload_dir = Helper.mvc_dir('public/uploads/img/blog')

                listext = ['png', 'jpg', 'JPG', 'jpeg']
                dimension = {550: 446, 770: 450}
                size = 1024 * 1024 * 2  # 2MB File Size Allowed Only
                ext = file.ext(feature_image.filename)

                upload = file.Image(upload_dir, feature_image)

                
                rename = str(pagepara) + str(Helper.rand(6))
                

                newfile_name = rename + upload.filename
                

                if ext in listext:
                    if size >= upload.size():

                        for w, h in dimension.items():
                            upload.resize(w, h, rename)
                            
                        # update profile image
                        respons_img = file.upload(feature_image, upload_dir, rename)
                        

                    else:
                        msg = " <div class='alert alert-danger material_alert material_alert_danger' > <button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>x</span></button>  Enter Page Content </div>"
                else:
                    msg = " <div class='alert alert-danger material_alert material_alert_danger' > <button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>x</span></button>  invalid Image File </div>"
            else:
                msg = ""
            info = [{
                "blog_para": pagepara,
                "blog_title": pagename,
                "blog_content": pagecontent,
                "blog_img": newfile_name,
                "admin_id": 1,
                "blog_status": 'PENDING' if status == "" else "APPROVED",
                "blog_createddate": Web.Functions().datetime(),
            }]
            response = Blogs.update(info)
            

            if response is True:
                m.redirect(Web.url('/admin/blog/'))
                m.header()
            else:
                msg = " <div class='alert alert-danger ' > <button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>x</span></button>  Unable to process this action, try again later </div>"

    blogr = Blogs.id(id)
    
    if  blogr[0] > 0:
        data = {
            'title': "Beta Codings",
            'blog_title': blogr[1][0]["blog_title"],
            'blog_para': blogr[1][0]["blog_para"],
            'blog_lang': blogr[1][0]["blog_lang"],
            'blog_img': blogr[1][0]["blog_img"],
            'blog_id': blogr[1][0]["blog_id"],
            'blog_content': blogr[1][0]["blog_content"],
            'blogcount': blogr[0],
            'msg': msg,
        }

        m.views('admin/updateblog', data)
    else:
        m.redirect(Web.url('admin/blog'))

