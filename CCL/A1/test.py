# content 2b sent will be decided by webapp2
import webapp2


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write("Hello World")


# WISGI server routes a particular request to this app
app = webapp2.WSGIApplication([('/', MainPage), ], debug=True)
