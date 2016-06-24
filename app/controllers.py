from system.mvc import Controller
from system.http import Cookie
from system.html import Table
from importlib import import_module
from inspect import getfullargspec
from inspect import getmembers
from inspect import isclass
from system.log import Output
class Index(Controller):
    
    def getLibrary(self):
        modules = [
            'system.html',
            'system.http',
            'system.log',
            'system.mvc',
            'system.routing',
            'system.template',
            'system.view',
            'system.web',
        ]
        
        library = ''
        for module in modules:
            mod = import_module(module)
            library += '<div><h3>' + module + '</h3>'
            library += '<ul>'
            for name, obj in getmembers(mod):
                if isclass(obj):
                    if obj.__module__ == module:
                        library += '<li><a href="/library/system.http.' + name +'">' + name + '</a></li>'
                        pass
            library += '</ul></div>'
        return library
            
                        
    def index(self):
        
        return self.view({
            'library' : self.getLibrary()
        })

    def download(self, user):

        self.response.getCookies().add(Cookie('Test', 'value'))
        self.response.getCookies().add(Cookie('Test', 'value;=dsadas;'))

        return self.view({
            'user': user
        })
        
    def library(self, lib):
        
        segments = lib.split('.')
        module = segments[0]
        className = segments[1]
        
        package = import_module('system.'+ module)
        cls = getattr(package, className)()
        attrs = (dir(cls))
        
        vTable = Table();
        vTable.setAttributes({ 'class' : 'grid'})
        vTable.addHeader('description', 'Description')
        
        for attr in attrs:
            if attr[0:1] !="_":
                pass
                methodSig = getfullargspec(getattr(cls, attr))
                
                strArg = ''
                for arg in methodSig.args:
                    if arg !='self':
                        strArg += '<label>'+arg + "</label>, "
                        
                vTable.addRow({'description' : '<h3>'+attr + "(" + strArg.strip(' ,') + ")</h3>" + str(getattr(cls, attr).__doc__)})

        return self.view({
            'vTable' : vTable.render(),
            'library' : self.getLibrary()
        })