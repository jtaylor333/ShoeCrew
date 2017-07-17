from google.appengine.ext import ndb

class ShoeU(ndb.Model):
    shoe_name = ndb.StringProperty()
    shoe_description = ndb.StringProperty()
    