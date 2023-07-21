import web
import os

urls = ("/", "index", "/heartbeat.jsp", "heartbeat")
app = web.application(urls, globals())
render = web.template.render('templates', globals={'os': os, 'ext':ext})


class index:
    def GET(self):
        return render.index()

class heartbeat:
    def POST(self):
        data = web.data()
        return "classic17.net"
        with open("logs.txt", "a") as f:
            f.write(str(data))
    def GET(self):
        return "Unauthorised"

if __name__ == "__main__":
    app.run()
