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

        new_shoe = shoe_upload.ShoeU.query().fetch()
       
        posts = ""
        for post in new_shoe:
            posts += "<div>"
            posts += "<h3>User : " + post.user + "</h3>"
            posts += "<h3>User : " + post.shoe_name + "</h3>"
            posts += "<p>" + post.shoe_description + "</p>"
            posts += "<img src =" + post.shoe_link + ">"
            posts += "</div>"




    	# do stuff with books...
        html_params = {
            "title": "Upload",
            "content": "Upload your kicks here",
            "html_post": posts,
        }



    def post(self):
        user = users.get_current_user()
        if user != None:
            r_name = self.request.get("name")
            r_desc = self.request.get("description")
            r_piclink = self.request.get("piclink")



            logging.info("contents was "+r_contents)

            new_post = Comment(user=user.email(), contents=shoe_name, )
            new_comment.put()


        template = jinja_env.env.get_template('templates/tmpl.html')
        self.response.out.write(template.render(html_params))

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
    #        self.redirect("/all")