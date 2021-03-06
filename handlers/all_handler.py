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
            posts += "<div id=r>"
            posts += "<p class=i>Email: " + str(post.user_email) + "</p>"
            posts += "<p>Name: " + str(post.shoe_name) + "</p>"
            posts += "<p>" + str(post.shoe_description) + "</p>"
            posts += "<img src =" + str(post.shoe_link) + " height=300 width=300>"
            posts += "</div>"



        html_params = {
            "title": "All Shoes",
            "content": "Hello",
            "html_post": posts,
            "html_login_url": users.create_login_url('/all'),
        }


        user = users.get_current_user()

        if user != None:
            html_params["user_email"] = user.email()

        template = jinja_env.env.get_template('templates/tmpl4.html')
        self.response.out.write(template.render(html_params))
