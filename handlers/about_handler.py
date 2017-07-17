import logging
import webapp2
import jinja_env
from google.appengine.api import users


class AboutHandler(webapp2.RequestHandler):
    def get(self):
    	logging.info("AboutHandler")
        html_params = {
            "title": "",
            "content": "Hello"
        }
        template = jinja_env.env.get_template('templates/tmpl.html')
        self.response.out.write(template.render(html_params))