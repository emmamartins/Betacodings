from pytonik import Web as mvc
from pytonik.Functions.ip import ip
from pytonik.Functions.now import now
from pytonik.Functions.agent import os, browser

m = mvc.App()
Blogs = mvc.Load('Blog')
Testimonies = mvc.Load('Testimonies')
Pages = mvc.Load('Pages')
Service = mvc.Load('Service')
views = mvc.Load('Views')
pagination = mvc.Pagination()
date = now()
oss = os()
brow = browser()


def blog(Request):
	#m.header()
	if Request.method == "GET":
		
		code = Request.params('code')
		if code is not "":
			p = Request.params('page')
			if p is not "":
				para = int(p)
			else:
				para = 1

			num_per_page = 3

			start = 1 if (para - 1) < 1 else (para - 1)

			start_page = start * num_per_page

			listBlog = Blogs.list('APPROVED', start_page, num_per_page, code)
			blog = Blogs.status('APPROVED', code)
			total = int(float(blog[0] + (num_per_page - 1)) / float(num_per_page))
			listTestimony = Testimonies.list(1, 3)
			
			listCode = Blogs.codes('APPROVED')
			listservice = Service.list('APPROVED')
			data = {
				'title': "pytonik MVC",
				'url': mvc.url(),
				'countTestimony': listTestimony[0],
				'listTestimony': listTestimony[1],
				'url': mvc.url(),
				'code': str(code).lower(),
				'listCode': listCode[1],
				'oldformat': '%Y-%m-%d %H:%M:%S',
				'newformat': '%d %B %Y',
				'listservice': listservice[1],
				'listBlog': listBlog[1],
				'listblog': listBlog[1],
				'countBlog': listBlog[0],
				'paging': pagination.number(total=total, page=para, url='/blog/{code}'.format(code=code), css=['pagination pagination-lg justify-content-center mb-1', 'page-item',
																					'page-link'])

			}
			m.views('home/blog', data)
		else:
			
			m.redirect(mvc.url('/404'))
	else:
		
		m.redirect(mvc.url('/404'))



def index(Request):
	#Request = mvc.Request()
	if Request.method == "GET":
		p = Request.params('page')
		if p is not "":
			para = int(p)
		else:
			para = 1

	num_per_page = 10

	start = 1 if (para - 1) < 1 else (para - 1)

	start_page = start * num_per_page

	listBlog = Blogs.list('APPROVED', start_page, num_per_page)
	blog = Blogs.status('APPROVED')
	total = int(float(blog[0] + (num_per_page - 1)) / float(num_per_page))
	listTestimony = Testimonies.list(1, 3)
	
	listCode = Blogs.codes('APPROVED')
	listservice = Service.list('APPROVED')
	data = {
		'title': "pytonik MVC",
		'url': mvc.url(),
		'countTestimony': listTestimony[0],
		'listTestimony': listTestimony[1],
		'url': mvc.url(),
		'listCode': listCode[1],
		'oldformat': '%Y-%m-%d %H:%M:%S',
		'newformat': '%d %B %Y',
		'listservice': listservice[1],
		'listBlog': listBlog[1],
		'listblog': listBlog[1],
		'countBlog': listBlog[0],
		'paging': pagination.number(total=total, page=para, url='/p', css=['pagination pagination-lg justify-content-center mb-1', 'page-item',
																			  'page-link'])

	}
	m.views('home/index', data)


def read(Request):

	if Request.method == "GET":
		para = Request.params('para')
		blog = Blogs.para(para)
		if blog[0] > 0:

			visitors = ip().get()
			ipv = visitors.ip
			hostname = visitors.hostname
			city = visitors.city
			region = visitors.region
			country = visitors.country
			loc = visitors.loc
			org = visitors.org
			idv = blog[1][0]["blog_id"]
			listViews = views.list(ipv, idv)

			if listViews[0] > 0:

				if listViews[1][0]["blogviews_date"] != date.date('%d-%m-%Y'):
					typed = "return"
					info = [{
						'blog_id': para,
						'blogviews_ip': ipv,
						'blogviews_date': date.date('%d-%m-%Y'),
						'blogviews_time': date.time(),
						'blogviews_type': typed,
						'blogviews_country': country,
						'blogviews_city': city,
						'blogviews_region': region,
						'blogviews_browsername': brow.name,
						'blogviews_browserversion': brow.version,
						'blogviews_os': oss.name,
						'blogviews_org': org,
						'blogviews_loc': loc,
					}]
					response = views.insert(info)

			else:
				typed = 'new'
				info = [{
					'blog_id': idv,
					'blogviews_ip': ipv,
					'blogviews_date': date.date('%d-%m-%Y'),
					'blogviews_time': date.time(),
					'blogviews_type': typed,
					'blogviews_country': country,
					'blogviews_city': city,
					'blogviews_region': region,
					'blogviews_browsername': brow.name,
					'blogviews_browserversion': brow.version,
					'blogviews_os': oss.name,
					'blogviews_org': org,
					'blogviews_loc': loc,
				}]
				response = views.insert(info)

			listBlog = Blogs.list('APPROVED', 1, 2)
			data = {
				'title': "{}".format(blog[1][0]["blog_title"]),
				'blogtitle': blog[1][0]["blog_title"],
				'blogcontent': blog[1][0]["blog_content"],
				'blogcreateddate': blog[1][0]["blog_createddate"],
				'blog_id': blog[1][0]["blog_id"],
				'blog_para': blog[1][0]["blog_para"],
				'blog_lang': blog[1][0]["blog_lang"],
				'admin_id': blog[1][0]["admin_id"],
				'listblog': listBlog[1],
				'oldformat': '%Y-%m-%d %H:%M:%S',
				'newformat': '%d %B %Y',
			}
			m.views('home/singlepost', data)
		else:
			m.redirect(mvc.url('/404'))

	else:
		m.redirect(mvc.url('/404'))


def request(Request):

	m.header()
	if Request.method == "POST":
		para = Request.post('para')

	data = {
		'title': "Request Project - ",

	}
	m.views('home/request', data)


def page(Request):

	m.header()
	if Request.method == "GET":
		para = Request.params('para')
		if para is not "":

			page = Pages.get(para, "approve")

			if page[0] > 0:
				listBlog = Blogs.list('APPROVED', 1, 3)
				data = {
					'title': "Request Project - ",
					'pagetitle': page[1][0]["title"],
					'listblog': listBlog[1],
					'pagecontent': page[1][0]["content"],
					'oldformat': '%Y-%m-%d %H:%M:%S',
					'newformat': '%d %B %Y',

				}

				m.views('home/page', data)

			else:
				m.redirect(mvc.url('/404'))
		else:
			m.redirect(mvc.url('/404'))
	else:
		m.redirect(mvc.url('/404'))


def contact(Request):
	m.header()
	if Request.method == "POST":
		email = Request.post('email')
		name = Request.post('name')
		message = Request.post('message')
		attachment = Request.post('attachment')

	data = {
		'title': "Request Project - ",

	}

	m.views('home/contact', data)

def contributor(Request):
	#m.header()
	if Request.method == "POST":
		email = Request.post('email')
		name = Request.post('name')
		phone = Request.post('name')
		country = Request.post('name')
	
	data = {
		'title': "Request Project - ",

	}

	m.views('home/contributor', data)
