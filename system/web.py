from importlib import import_module
from system.routing import RouteCollection
from system.http import HttpRequest
from system.http import HttpResponse
from system.mvc import StringResult

class HttpApplication():
    
    def __init__(self, rootPath):
        self.rootPath = rootPath
        self.routes = RouteCollection()
        self.request = HttpRequest()
        self.response = HttpResponse()
        
    def load(self):
        pass

    def run(self):
        if len(self.routes) == 0:
            raise Exception("One or more routes must be registered.")
        
        controllerFound = False
        for route in self.routes:
            routeParams = route.execute(self.request)
            
            if len(routeParams) > 0:
                self.request.setRouteData(routeParams)
                
                package = import_module('app.controllers')
                className = getattr(package, routeParams['controller'])
                controller = className(self.rootPath)
                controller.setHttpRequest(self.request)
                controller.setHttpResponse(self.response)
                action = getattr(controller, routeParams['action'])
                result = action();
                
                if type(result) is str:
                    result = StringResult(result)
                    
                controller.render(result)
                controllerFound = True
                break
                
        if controllerFound == False:
            raise Exception('Unable to map the request to a controller/action.')

    def end(self):
        self.response.flush()
        
    def error(self, e):
        self.response.write(str(e)).flush()