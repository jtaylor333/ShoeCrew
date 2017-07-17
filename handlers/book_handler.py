import jinja_env
import logging
import webapp2
from models import shoe_upload

from models import book
from google.appengine.api import users

class BookHandler(webapp2.RequestHandler):
    def get(self):
    	logging.info("SecondHandler")
    	books = book.Book.query().fetch()
    	# do stuff with books...
        html_params = {
            "title": "Upload",
            "content": "Upload your kicks here"
        }

        user = users.get_current_user()

        if user != None:
            html_params["user_email"] = user.email()

        template = jinja_env.env.get_template('templates/tmpl.html')
        self.response.out.write(template.render(html_params))

    def post(self):
            
        r_name = self.request.get("name")
        r_description = self.request.get("description")
            # logging.info(r_name)

        new_shoe = shoe_upload.ShoeU(

            shoe_name = r_name,
            shoe_description = r_description,
            user_email = "Fix Later",
              


            )
           new_shoe.put()
           self.redirect("/all")