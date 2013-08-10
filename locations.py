import config
import json
import operator

from twitter_location import twitter_location
from foursquare_location import foursquare_location
from flickr_location import flickr_location

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

f = open('recent_location.json', 'w')
f.write(json.dumps(location))

print "Go here: http://maps.googleapis.com/maps/api/staticmap?zoom=13&size=600x300&maptype=roadmap&markers=color:blue%7Clabel:S%7C" + str(location["latitude"]) + "," + str(location["longitude"]) + "&sensor=false"
