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
 
		"""
		_________                _____.__
		\_   ___ \  ____   _____/ ____\__| ____
		/    \  \/ /  _ \ /    \   __\|  |/ ___\
		\     \___(  <_> )   |  \  |  |  / /_/  >
		 \______  /\____/|___|  /__|  |__\___  /
		        \/            \/        /_____/
		
		You will need to grab the various tokens to go forward. I tried to make it
		as easy as possible.
		
		"""
		
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
		
		#amazon aws
		amazon_s3_bucket_name = 'my_location_bucket'
		amazon_access_key = ""
		amazon_secret_access_key = ""
		
		#filename
		recent_location_filename = "recent_location.json"
 
###Run the bad boy

####Drop a local file with location

 * You can run each of the scripts individually to make sure they work: `python foursquare_location.py`
	
		harper@ {~/instant-location}$ python foursquare_location.py
		<__main__.foursquare_location object at 0x10828d710>
		{'date': '2013-08-09 19:38:24', 'source': 'foursquare', 'id': 1376095104, 'longitude': -87.68533102506872, 'latitude': 41.91035473476432}
		1376095104
 * Once you are confident it works correctly go ahead and run the main `locations.py` script
 
		harper@ {~/instant-location}$ ./location_to_file.py
		http://maps.googleapis.com/maps/api/staticmap?zoom=13&size=600x300&maptype=roadmap&markers=color:blue%7Clabel:S%7C41.91008943,-87.68528519&sensor=false

	This outputs a map url of your last known location. Whee. 
	
	It also drops `recent_location.json`
	
	The `recent_location.json` has your most recent location!
	
####Upload file to an s3 bucket

You can do the same thing as dropping a local file, but you push the file to an s3 bucket. 

The first step is to make sure your config file has your AWS keys, and bucket name. The bucket can exist, but it will set the generated file as public. 

Once you run the script `location_to_s3.py`, the file will be uploaded to the bucket and BAM - you have a publicly accessible JSON file with your location. 

		harper@ {~/instant-location}$ ./location_to_s3.py
		S3 URL: https://my_location_bucket.s3.amazonaws.com/recent_location.json

Publicly Accessible:

		harper@ {~/instant-location}$ curl https://my_location_bucket.s3.amazonaws.com/recent_location.json
		{"date": "2013-08-12 03:10:38", "source": "twitter", "id": 366758599919284224, "longitude": -87.6755019, "latitude": 41.90907876}%

This is how we will be using this to upload location data for inclusion in a map of our friends. 
	
##Next steps
There is a lot of places that could be made more efficient or better. Feel free to fix it up. 

Here are my thoughts: 

 * ~~cronable script to post recent_location.json to s3~~
 * facebook support
 * instagram support
 * site generator for something similar to [http://wheres.broox.com/](http://wheres.broox.com/)
 
 Other ideas?

##Motivation

My buddy Derek Brooks has an amazing geo setup on his site. I always follow his lead and have replicated it on my site. This works well, but is about 200 terrible scripts. We wanted to add location for a couple other people and so i whipped up a stand alone script. 

This is going ot be used to power a map of [my awesome coworkers](http://ltc.io).

##Harper is awesome. 
hit me up: [@harper](http://twitter.com/harper) ([harper@nata2.org](mailto:harper@nata2.org))
