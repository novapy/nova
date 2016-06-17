from os import path
from abc import ABC
from system.template import Lexer
from system.template import Compiler

class View(ABC):
    
    def setData(self, data):
        self.data = data
    
    def setHttpRequest(self, request):
        self.request = request

class StringTemplate(View):
    
    def __init__(self, rootPath):
        self.rootPath = rootPath
        
    def render(self):
        routeData = self.request.getRouteData()
        viewFile = "{rootPath}/app/views/{controller}/{action}.tpl".format(
            rootPath = self.rootPath, 
            controller = routeData['controller'].lower(), 
            action = routeData['action'].lower()
        )

        if path.isfile(viewFile):
            f = open(viewFile)
            lexer = Lexer(f.read())
            return Compiler.compile(self.rootPath, lexer.getTokens(), self.data)
        else:
            raise Exception("View file not found " + viewFile)