import foursquare
import datetime
from social_location import location


class foursquare_location(location):
    def __init__(
        self,
        foursquare_client_id,
        foursquare_client_secret,
        foursquare_redirect_uri,
        foursquare_access_token
    ):
        # Construct the client object
        self.client = foursquare.Foursquare(client_id=foursquare_client_id, client_secret=foursquare_client_secret)
        self.client.set_access_token(foursquare_access_token)

    def get_location(self):
        # Get the user's data

        since_id = self.get_last_id()  # "365956221922066432"
        params={'limit': 1, "sort":"newestfirst"}

        if since_id:
            params["afterTimestamp"] = since_id

        last_checkin = self.client.users.checkins(params=params)

        foursquare_location = {}
        foursquare_location['source'] = 'foursquare'
        foursquare_location['id'] = last_checkin['checkins']['items'][0]['createdAt']
        foursquare_location['date'] = str(datetime.datetime.fromtimestamp(int(last_checkin['checkins']['items'][0]['createdAt'])))
        foursquare_location['latitude'] = last_checkin['checkins']['items'][0]['venue']['location']['lat']
        foursquare_location['longitude'] = last_checkin['checkins']['items'][0]['venue']['location']['lng']
        return foursquare_location


if __name__ == "__main__":
    import config
    location_obj = foursquare_location(
        config.foursquare_client_id,
        config.foursquare_client_secret,
        config.foursquare_redirect_uri,
        config.foursquare_access_token
    )
    print location_obj
    print location_obj.location()
    print location_obj.get_last_id()

