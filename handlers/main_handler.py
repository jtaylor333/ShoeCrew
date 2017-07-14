
import jinja_env
import logging
import webapp2

from google.appengine.api import users

class MainHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("MainHandler")
        logging.info(users.get_current_user())
        logging.info(users.create_login_url('/'))

        html_params = {
            "title": "Shoe Crew",
            "content": "It works",
            "html_login_url": users.create_login_url('/'),
        }

        user = users.get_current_user()

        if user != None:
            html_params["user_email"] = user.email()

        template = jinja_env.env.get_template('templates/tmpl2.html')
        self.response.out.write(template.render(html_params))
