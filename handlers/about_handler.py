import jinja_env
import logging
import webapp2

from google.appengine.api import users

	


class AboutHandler(webapp2.RequestHandler):
    def get(self):
    	logging.info("AboutHandler")
        html_params = {
            "title": "About Page",
            "content": "Hello, we are the Shoe Crew.",
            "html_login_url": users.create_login_url('/about'),
        }

        user = users.get_current_user()

        if user != None:
            html_params["user_email"] = user.email()


        template = jinja_env.env.get_template('templates/tmpl3.html')
        self.response.out.write(template.render(html_params))