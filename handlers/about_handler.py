import jinja_env
import logging
import webapp2

from google.appengine.api import users




class AboutHandler(webapp2.RequestHandler):

	<link rel="stylesheet" type="text/css" href="resources/style.css">
	<link rel="stylesheet" type="text/css" href="resources/title.css">
	
    def get(self):
    	logging.info("AboutHandler")
        html_params = {
            "title": "About Page",
            "content": "Hello, we are the Shoe Crew."
        }
        template = jinja_env.env.get_template('templates/tmpl3.html')
        self.response.out.write(template.render(html_params))