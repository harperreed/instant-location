import json


class location(object):

    def cache_name(self):
        return self.__class__.__name__ + '_location.json'

    def get_last_id(self):
        try:
            f = open(self.cache_name(), 'r')
            location = json.loads(f.read())
            if location:
                return location['id']
            else:
                return None
        except:
            return None

    def get_last_location(self):
        try:
            f = open(self.cache_name(), 'r')
            location = json.loads(f.read())
            return location
        except:
            return None

    def cache(self):
        f = open(self.cache_name(), 'w')
        f.write(json.dumps(self.location_obj))

    def location(self):
        self.location_obj = self.get_location()
        if self.location_obj:
            self.cache()
            return self.location_obj
        else:
            return self.get_last_location()



    def get_location(self):
        return None
