import os
import cgi

class HttpRequest():

    def __init__(self):
        self.uri = os.environ["REQUEST_URI"].strip('/')
        self.segments = self.uri.split("/");
        self.post = cgi.FieldStorage()
        self.routeData = {}
        
    def getUri(self):
        return self.uri
            
    def getSegment(self, index):
        try:
            return self.segment[index]
        except IndexError:
            pass
        
    def isGet(self):
        if os.environ["REQUEST_METHOD"] == 'GET':
            return True
        return False
        
    def isPost(self):
        if os.environ["REQUEST_METHOD"] == 'POST':
            return True
        return False
    
    def getPost(self, name, default):
        return self.post.getvalue(name, default)
    
    def setRouteData(self, data):
        self.routeData = data
    
    def getRouteData(self):
        return self.routeData
    
    
class HttpResponse():
    
    def __init__(self):
        self.contentType = 'text/html'
        self.contentEncoding = 'UTF-8'
        self.output = ''
    
    def setContentType(self, contentType):
        self.contentType = contentType
        return self
    
    def setContentEncoding(self, contentEncoding):
        self.contentEncoding = contentEncoding
        return self
    
    def write(self, output):
        self.output = output
        return self
    
    def flush(self):
        print("Content-type: " + self.contentType + ";charset=" + self.contentEncoding)
        print("")
        print(self.output)