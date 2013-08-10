import twitter
import datetime
import time
from social_location import location

class twitter_location(location):
    def __init__(
        self,
        twitter_consumer_key,
        twitter_consumer_secret,
        twitter_access_token_key,
        twitter_access_token_secret
    ):
        self.api = twitter.Api(
            consumer_key=twitter_consumer_key,
            consumer_secret=twitter_consumer_secret,
            access_token_key=twitter_access_token_key,
            access_token_secret=twitter_access_token_secret
        )

    def get_location(self):

        twitter_since_id = self.get_last_id()  # "365956221922066432"

        try:
            twitter_status = self.api.GetUserTimeline(
                count=100,
                since_id=twitter_since_id
            )
        except:
            return None

        place_holder = 0
        last_twitter_status = None

        if twitter_status:
            while (last_twitter_status == None):
                try:
                    twitter_status[place_holder].geo['coordinates'][0]
                    last_twitter_status = twitter_status[place_holder]
                except:
                    place_holder = place_holder + 1

            twitter_location = {}
            twitter_location['source'] = 'twitter'
            twitter_location['id'] = last_twitter_status.id
            twitter_location['date'] = str(datetime.datetime(*time.strptime(last_twitter_status.created_at,'%a %b %d %H:%M:%S +0000 %Y')[0:6]))
            twitter_location['latitude'] = last_twitter_status.geo['coordinates'][0]
            twitter_location['longitude'] =last_twitter_status.geo['coordinates'][1]
        else:
            twitter_location = None

        return twitter_location

if __name__ == "__main__":
    import config
    location_obj = twitter_location(
        config.twitter_consumer_key,
        config.twitter_consumer_secret,
        config.twitter_access_token_key,
        config.twitter_access_token_secret
    )
    print location_obj
    print location_obj.location()
    print location_obj.get_last_id()
