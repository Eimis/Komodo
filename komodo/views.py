from django.shortcuts import render
import json
import urllib2




def Main(request):
	if request.method == 'GET':
		return render(request, 'main.html', {})

def Search(request):
	json_data = urllib2.urlopen('http://127.0.0.1:8000/static/test.json/')
	data = json.load(json_data)
	blah = data[0][u'threads'][0][u'com']
	#blah = data
	q = request.POST['q']
	#result_list = [thread for thread in data if thread['page'] == q]
	result_list = []
	for x in data:
		for y in x[u'threads']:
				z = y.get(u'com') # .get() is required because some threads only contain images (no com)
				result_list.append(z)
	testy = u'Python' in result_list
	return render(request, 'search.html',{"q" : q, "result_list" : result_list, "blah" : blah, "data" : data, "testy" : testy, })