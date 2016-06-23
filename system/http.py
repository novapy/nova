import os
import cgi
from collections import Sequence
from urllib import parse

class HttpRequest():

    def __init__(self):
        self._uri = os.environ["REQUEST_URI"].strip('/')
        self._segments = self._uri.split("/");
        self._post = {}

        form = cgi.FieldStorage()
        for k in form.keys():
            self._post[k] = form.getvalue(k)
        
        self._routeData = {}
        self._params = self._post
        
    def getUri(self):
        '''Gets the request uri'''
        return self._uri
            
    def getSegment(self, index):
        '''Gets a uri segment using the specified index.'''
        try:
            return self.segments[index]
        except IndexError:
            return False
        
    def isGet(self):
        if os.environ["REQUEST_METHOD"] == 'GET':
            return True
        return False
        
    def isPost(self):
        if os.environ["REQUEST_METHOD"] == 'POST':
            return True
        return False
    
    def getPost(self, name):
        return self._post[name]
    
    def setParam(self, name, value):
        self._params[name] = value
    
    def getParam(self, name):
        return self._params[name]
    
    def setRouteData(self, data):
        self._routeData = data
    
    def getRouteData(self):
        return self._routeData
    
    def toArray(self):
        return self._params
    
class HttpResponse():
    
    def __init__(self):
        self.contentType = 'text/html'
        self.contentEncoding = 'UTF-8'
        self.output = ''
        self.cookies = CookieCollection()
    
    def setContentType(self, contentType):
        self.contentType = contentType
        return self
    
    def setContentEncoding(self, contentEncoding):
        self.contentEncoding = contentEncoding
        return self
    
    def write(self, output):
        self.output = output
        return self
    
    def getCookies(self):
        return self.cookies;
    
    def flush(self):
        print("Content-type: " + self.contentType + ";charset=" + self.contentEncoding)
        
        for cookie in self.cookies:
            print("Set-Cookie: {0}={1}; path={2}".format(parse.quote(cookie.getName()), parse.quote(cookie.getValue()), parse.quote(cookie.getPath())))
        print("")
        print(self.output)
        
class CookieCollection(Sequence):
    
    def __init__(self):
        self.collection = []
        
    def __getitem__(self, index):
        return self.collection[index]
    
    def __len__(self):
        return len(self.collection)
        
    def add(self, cookie):
        self.collection.append(cookie)
        
class Cookie():
    
    def __init__(self, name = None, value = None):
        self.name = name;
        self.value = value;
        self.path = '/'
        
    def setName(self, name):
        self.name = name
        
    def getName(self):
        return self.name
    
    def setValue(self, name):
        self.value = name
        
    def getValue(self):
        return self.value
    
    def setPath(self, path):
        self.path = path
        
    def getPath(self):
        return self.path