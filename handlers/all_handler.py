import jinja_env
import logging
import webapp2

from google.appengine.api import users

class AllHandler(webapp2.RequestHandler):
    def get(self):
    	logging.info("AllHandler")
        html_params = {
            "title": "All Shoes",
            "content": "Hello"
        }
        template = jinja_env.env.get_template('templates/tmpl3.html')
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