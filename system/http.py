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
        '''Gets the request uri.'''
        
        return self._uri
            
    def getSegment(self, index):
        '''Gets a uri segment using the specified index.'''
        
        try:
            return self.segments[index]
        except IndexError:
            return False
        
    def isGet(self):
        '''Gets a boolean value that determins if the request is a GET.'''
        
        if os.environ["REQUEST_METHOD"] == 'GET':
            return True
        return False
        
    def isPost(self):
        '''Gets a boolean value that determins if the request is a POST.'''
        
        if os.environ["REQUEST_METHOD"] == 'POST':
            return True
        return False
    
    def getPost(self, name):
        '''Gets the value of a post field using the specified name.'''
        
        return self._post[name]
    
    def setParam(self, name, value):
        '''Sets a param field using the specified name and value.'''
        self._params[name] = value
    
    def getParam(self, name):
        '''Gets the value of a param field using the specified name.'''
        
        return self._params[name]
    
    def setRouteData(self, data):
        '''Sets route data for the current request.
        This method is not intended to be used directly.''' 
        
        self._routeData = data
    
    def getRouteData(self):
        '''Gets a dict of all route data.'''
        
        return self._routeData
    
    def toArray(self):
        '''Gets a dict of all params.'''
        
        return self._params
    
class HttpResponse():
    
    def __init__(self):
        self._contentType = 'text/html'
        self._contentEncoding = 'UTF-8'
        self._output = ''
        self._cookies = CookieCollection()
    
    def setContentType(self, contentType):
        self._contentType = contentType
        return self
    
    def setContentEncoding(self, contentEncoding):
        self._contentEncoding = contentEncoding
        return self
    
    def write(self, output):
        self._output = output
        return self
    
    def getCookies(self):
        return self._cookies;
    
    def flush(self):
        print("Content-type: " + self._contentType + ";charset=" + self._contentEncoding)
        
        for cookie in self._cookies:
            print("Set-Cookie: {0}={1}; path={2}".format(parse.quote(cookie.getName()), parse.quote(cookie.getValue()), parse.quote(cookie.getPath())))
        print("")
        print(self._output)
        
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