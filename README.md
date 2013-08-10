#instant location 
##A terrible and slow replacement for the sadly departed latitude API


Grab your social checkins, tweets, photos and store the last known location.

Ever since latitude was pulled and the API stopped working I decided to grab
my location from the social interactions instead of the no longer working
latitude api.

I have code similar to this running to store my current location and
power [http://harperreed.com/location](http://harperreed.com/location).

I tried to make it as simple as possible to support new apps that store
location. Feel free to add a facebook class.

Use it and hit me up: [@harper](http://twitter.com/harper) ([harper@nata2.org](mailto:harper@nata2.org))

##How to use it

###Requirements
You will need to install these things

 * `easy_install python-twitter`
 * `easy_install foursquare`
 * `easy_install python-flickr`
 
###Configure the app

 * rename the `config.py.example` to `config.py`
 * fill out all the goodies in `config.py`
 
		 #Twitter API Tokens
		#Get creds
		#https://dev.twitter.com/apps/new
		twitter_consumer_key = ""
		twitter_consumer_secret = ""
		twitter_access_token_key = ""
		twitter_access_token_secret = ""
		
		#Foursquare API Tokens
		#Get creds here:
		#https://foursquare.com/developers/register
		foursquare_client_id = ""
		foursquare_client_secret = ""
		foursquare_redirect_uri = ""
		foursquare_access_token = ""
		
		#Flickr API Tokens
		#Get creds here:
		#http://www.flickr.com/services/apps/create/noncommercial/?
		flickr_key = ""
		flickr_secret = ""
		flickr_oauth_token=""
		flickr_oauth_token_secret=""
		flickr_nsid = ""
 
###Run the bad boy
 * You can run each of the scripts individually to make sure they work: `ython foursquare_location.py`
	
		harper@ {~/instant-location}$ python foursquare_location.py
		<__main__.foursquare_location object at 0x10828d710>
		{'date': '2013-08-09 19:38:24', 'source': 'foursquare', 'id': 1376095104, 'longitude': -87.68533102506872, 'latitude': 41.91035473476432}
		1376095104
 * Once you are confident it works correctly go ahead and run the main `locations.py` script
 
		harper@ {~/instant-location}$ python locations.py
		http://maps.googleapis.com/maps/api/staticmap?zoom=13&size=600x300&maptype=roadmap&markers=color:blue%7Clabel:S%7C41.91008943,-87.68528519&sensor=false

	This drops a map url of your last known location. Whee. 
	
	It also drops two json files: `recent_locations.json` and `recent_location.json`
	
	The `recent_location.json` has your most recent location!
	
##Next steps
There is a lot of places that could be made more efficient or better. Feel free to fix it up. 

##Motivation

My buddy Derek Brooks has an amazing geo setup on his site. I always follow his lead and have replicated it on my site. This works well, but is about 200 terrible scripts. We wanted to add location for a couple other people and so i whipped up a stand alone script. 

This is going ot be used to power a map of [my awesome coworkers](http://ltc.io).

##Harper is awesome. 
hit me up: [@harper](http://twitter.com/harper) ([harper@nata2.org](mailto:harper@nata2.org))