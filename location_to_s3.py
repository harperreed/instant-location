import config
import json
import operator
import sys

from twitter_location import twitter_location
from foursquare_location import foursquare_location
from flickr_location import flickr_location

from boto.s3.connection import S3Connection
from boto.s3.key import Key

"""
.____                         __  .__
|    |    ____   ____ _____ _/  |_|__| ____   ____   ______
|    |   /  _ \_/ ___\\__  \\   __\  |/  _ \ /    \ /  ___/
|    |__(  <_> )  \___ / __ \|  | |  (  <_> )   |  \\___ \
|_______ \____/ \___  >____  /__| |__|\____/|___|  /____  >
        \/          \/     \/                    \/     \/

Grab your social checkins, tweets, photos and store the last known location.

Ever since latitude was pulled and the API stopped working I decided to grab
my location from the social interactions instead of the no longer working
latitude api.

I have code similar to this running to store my current location and
power (http://harperreed.com/location).

I tried to make it as simple as possible to support new apps that store
location. Feel free to add a facebook class.

Use it and hit me up: @harper (harper@nata2.org)

This script will drop a file in an s3 bucket and make it publicly accessible. This way you can grab it in another app.



"""


locations = []

twitter_location_obj = twitter_location(
    config.twitter_consumer_key,
    config.twitter_consumer_secret,
    config.twitter_access_token_key,
    config.twitter_access_token_secret)
locations.append(twitter_location_obj.location())

foursquare_location_obj = foursquare_location(
    config.foursquare_client_id,
    config.foursquare_client_secret,
    config.foursquare_redirect_uri,
    config.foursquare_access_token
)
locations.append(foursquare_location_obj.location())

flickr_location_obj = flickr_location(
    config.flickr_key,
    config.flickr_secret,
    config.flickr_oauth_token,
    config.flickr_oauth_token_secret,
    config.flickr_nsid
)
locations.append(flickr_location_obj.location())

location = sorted(locations, key=operator.itemgetter('date'), reverse=True)[0]

f = open(config.recent_location_filename, 'w')
f.write(json.dumps(location))

conn = S3Connection(config.amazon_access_key, config.amazon_secret_access_key)

try:
    bucket = conn.get_bucket(config.amazon_s3_bucket_name)
except:
    print "Creating bucket: " + config.amazon_s3_bucket_name
    bucket = conn.create_bucket(config.amazon_s3_bucket_name)
    print "Please run script again"
    sys.exit()


k = Key(bucket)
k.key = config.recent_location_filename
k.set_contents_from_string(json.dumps(location))
k.make_public()

print "S3 URL: https://" + config.amazon_s3_bucket_name + ".s3.amazonaws.com/" + config.recent_location_filename
