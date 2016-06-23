from inspect import getfullargspec
from importlib import import_module
from system.routing import RouteCollection
from system.http import HttpRequest
from system.http import HttpResponse
from system.mvc import StringResult
from system.log import Output
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
                
                actionArgs = getfullargspec(action).args
                compiledArgs = {}
                
                for arg in actionArgs:
                    if arg != "self":
                        try:
                            package = import_module('app.models')
                            model = getattr(package, arg)()
                            compiledArgs[arg] = model
                        except:
                            compiledArgs[arg] = None

                        for param in self.request.toArray():

                            if param.find('.') > -1:
                                objName = param[0: param.index('.')]
                                fieldName = param[param.index('.')+1:]
                                
                                if objName == arg:
                                    if (hasattr(model, fieldName)):
                                        setattr(model, fieldName, self.request.getParam(param))

                                        compiledArgs[arg] = model
                            
                            else: 
                                compiledArgs[arg] = self.request.getParam(arg)
                                                                                   
                result = action(**compiledArgs);

                if type(result) is str:
                    result = StringResult(result)
                elif type(result) is dict:
                    result = StringResult(str(result))
                elif type(result) is list:
                    result = StringResult(str(result))
                    
                controller.render(result)
                controllerFound = True
                break
                
        if controllerFound == False:
            raise Exception('Unable to map the request to a controller/action.')

    def end(self):
        self.response.flush()
        
    def error(self, e):
        self.response.write(str(e)).flush()