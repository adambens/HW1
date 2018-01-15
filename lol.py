import requests
import json


import urllib.request, urllib.parse, urllib.error

location = input('enter location: ')

darkskybaseurl = "https://api.darksky.net/forecast/"
darkskykey = "3b57dd52a8686931c7dbcd8deed3f000"
dparams = {}
dparams['key'] = darkskykey
googlebaseurl = "https://maps.googleapis.com/maps/api/geocode/json?"
googlekey = "AIzaSyBUyCIRN5GBTyznebbKTpeL6bJydO8NQGs"
gparams = {}
gparams['key'] = googlekey
#if request.method == 'POST':
#location = request.form['location']
gparams['address'] = location
googledata = requests.get(googlebaseurl, params = gparams)
googlelocation = json.loads(googledata.text)
lat = googlelocation["results"][0]["geometry"]["location"]["lat"]
lng = googlelocation["results"][0]["geometry"]["location"]["lng"]
#dparams['latitude'] = lat
#dparams['longitude'] = lng
#darkskydata = requests.get(darkskybaseurl, params=dparams)
#forecast = json.loads(darskydata.text)
#print(forecast)
#print(darkskydata.text)
print(lat,lng)


"""
darkskybaseurl = "https://api.darksky.net/forecast/"
	darkskykey = "3b57dd52a8686931c7dbcd8deed3f000"
	dparams = {}
	dparams['key'] = darkskykey
	googlebaseurl = "https://maps.googleapis.com/maps/api/geocode/json?"
	googlekey = "AIzaSyBUyCIRN5GBTyznebbKTpeL6bJydO8NQGs"
	gparams = {}
	gparams['key'] = googlekey
	if request.method == 'POST':
		location = request.form['location']
		gparams['address'] = location
		googledata = requests.get(googlebaseurl, params = gparams)
		googlelocation = json.loads(googledata)
		lat = googlelocation["results"][0]["geometry"]["location"]["lat"]
		lng = googlelocation["results"][0]["geometry"]["location"]["lng"]
		dparams['latitude'] = lat
		dparams['longitude'] = lng
		darkskydata = requests.get(darkskybaseurl, params=dparams)
		forecast = json.loads(darkskydata)
		return formstr
	else:
		return "ok"


"""