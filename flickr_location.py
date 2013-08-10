from flickr import FlickrAPI
import datetime
from social_location import location

"""
___________.__  .__        __
\_   _____/|  | |__| ____ |  | _________
 |    __)  |  | |  |/ ___\|  |/ /\_  __ \
 |     \   |  |_|  \  \___|    <  |  | \/
 \___  /   |____/__|\___  >__|_ \ |__|
     \/                 \/     \/

Flickr last location grabber

"""


class flickr_location(location):
    def __init__(
        self,
        flickr_key,
        flickr_secret,
        flickr_oauth_token,
        flickr_oauth_token_secret,
        flickr_nsid
    ):

        self.api = FlickrAPI(
            api_key=flickr_key,
            api_secret=flickr_secret,
            oauth_token=flickr_oauth_token,
            oauth_token_secret=flickr_oauth_token_secret
        )
        self.flickr_nsid = flickr_nsid

    def get_location(self):

        recent_activity = self.api.get(
            'flickr.people.getPhotos',
            params={"user_id": self.flickr_nsid, "per_page": 20}
        )
        place_holder = 0
        last_flickr_photo = None
        last_photo_location = None

        if recent_activity:
            while not last_photo_location:
                try:
                    last_flickr_photo = self.api.get(
                        'flickr.photos.getInfo',
                        params={
                            "photo_id": recent_activity['photos']['photo'][place_holder]['id'],
                            "secret": recent_activity['photos']['photo'][place_holder]['secret']
                        }
                    )
                    last_photo_location = last_flickr_photo['photo']['location']

                except:
                    place_holder = place_holder + 1

        flickr_location = {}
        flickr_location['source'] = 'flickr'
        flickr_location['id'] = last_flickr_photo['photo']['id']
        flickr_location['date'] = str(datetime.datetime.fromtimestamp(int(last_flickr_photo['photo']['dateuploaded'])))
        flickr_location['latitude'] = last_photo_location['latitude']
        flickr_location['longitude'] = last_photo_location['longitude']
        return flickr_location

if __name__ == "__main__":
    import config
    location_obj = flickr_location(
        config.flickr_key,
        config.flickr_secret,
        config.flickr_oauth_token,
        config.flickr_oauth_token_secret,
        config.flickr_nsid
    )
    print location_obj
    print location_obj.get_last_id()
