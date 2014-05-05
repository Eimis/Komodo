from django.shortcuts import render
import json
import urllib2




def Main(request, slug):
	slug = slug
	if request.method == 'GET':
		return render(request, 'main.html', {"slug" : slug})

def Search(request, slug):
	slug = slug
	json_data = urllib2.urlopen('http://a.4cdn.org/' + slug + '/catalog.json')
	data = json.load(json_data)
	result_list = []
	link_list = []
	for page in data:
		for thread in page[u'threads']:
				post = thread.get(u'com') # .get() is required because some threads only contain images (no com)
				link = thread.get(u'no')
				result_list.append(post)
				link_list.append(link)
	q = request.POST['q']
	thread_list = zip(result_list, link_list)
	matching = [(post, link) for post, link in thread_list if post is not None and q.lower() in post.lower()] # not None - some threads only contain images (no text) and None = False in Python
	results = len(matching)
	return render(request, 'search.html',{"q" : q, "result_list" : result_list, "data" : data, "matching" : matching, "thread_list" : thread_list, "slug" : slug, "results" : results})

def server_error(request):
	# for some reason Django doesn't pass template variables ONLY to error500 page, so this view is required for serving static files for this page
    response = render(request, "500.html",{})
    response.status_code = 500
    return response

