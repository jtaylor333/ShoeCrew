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
        book_str = ""



    	# do stuff with books...
        html_params = {
            "title": "Upload",
            "content": "Upload your kicks here",
            
        }

        template = jinja_env.env.get_template('templates/upload.html')
        self.response.out.write(template.render(html_params))


    def post(self):
        user = users.get_current_user()
        if user != None:
            r_name = self.request.get("name")
            r_desc = self.request.get("description")
            r_piclink = self.request.get("piclink")




            new_post = shoe_upload.ShoeU(user_email=user.email(),
                                        shoe_name=r_name, 
                                        shoe_description=r_desc,
                                        shoe_link=r_piclink,
                                        )
            new_post.put()

        self.redirect("/all")



    # def post(self):
            
    #     r_name = self.request.get("name")
    #     r_description = self.request.get("description")
    #         # logging.info(r_name)

    #     new_shoe = shoe_upload.ShoeU(

    #         shoe_name = r_name,
    #         shoe_description = r_description,
    #         user_email = "Fix Later",
              


    #         )
    #        new_shoe.put()
          