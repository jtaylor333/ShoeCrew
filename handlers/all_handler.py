class AllHandler(webapp2.RequestHandler):
    def get(self):
    	logging.info("AllHandler")
        html_params = {
            "title": "",
            "content": "Hello"
        }
        template = jinja_env.env.get_template('templates/tmpl.html')
        self.response.out.write(template.render(html_params))