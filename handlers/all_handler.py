import jinja_env
import logging
import webapp2
from models import shoe_upload

from google.appengine.api import users

class AllHandler(webapp2.RequestHandler):
    def get(self):
    	logging.info("AllHandler")


        new_shoe = shoe_upload.ShoeU.query().fetch()
       
        posts = ""
        for post in new_shoe:
            posts += "<div>"
            posts += "<h3>User: " + str(post.user_email) + "</h3>"
            posts += "<h3>Shoe: " + str(post.shoe_name) + "</h3>"
            posts += "<p>" + str(post.shoe_description) + "</p>"
            posts += "<img src =" + str(post.shoe_link) + ">"
            posts += "</div>"

        html_params = {
            "title": "All Shoes",
            "content": "Hello",
            "html_post": posts,
        }


        template = jinja_env.env.get_template('templates/tmpl4.html')
        self.response.out.write(template.render(html_params))
