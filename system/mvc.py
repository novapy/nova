import json
from system.view import StringTemplate

class Controller():
    
    def __init__(self, rootPath):
        self.rootPath = rootPath
        self.viewEngine = StringTemplate(rootPath)
    
    def setHttpRequest(self, httpRequest):
        self.request = httpRequest
        
    def setHttpResponse(self, httpResponse):
        self.response = httpResponse
        
    def json(self, data):
        return JsonResult(self.response, data)
    
    def view(self, data = None, viewFile = None):
        if viewFile is not None:
            self.viewEngine.setViewFile(viewFile)
        
        self.viewEngine.setData(data)
        self.viewEngine.setHttpRequest(self.request)
        
        return ViewResult(self.viewEngine)
        
    def render(self, actionResult):
        self.response.write(actionResult.execute())


class ActionResult():
    
    def execute(self):
        pass
    
    
class StringResult(ActionResult):
    
    def __init__(self,data):
        self.data = data
        
    def execute(self):
        return self.data
    
    
class JsonResult(ActionResult):
    
    def __init__(self, httpResponse, data):
        self.response = httpResponse
        self.data = data
        
    def execute(self):
        self.response.setContentType('application/json').setContentEncoding('UTF-8')
        
        if isinstance(self.data, object):
            self.data = self.data.__dict__
            
        return json.dumps(self.data)
    
    
class ViewResult(ActionResult):
    
    def __init__(self,viewEngine):
        self.viewEngine = viewEngine;
        
    def execute(self):
        return self.viewEngine.render()