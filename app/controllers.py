from system.mvc import Controller
from system.http import Cookie
from system.html import Table
from importlib import import_module
from inspect import getfullargspec
from inspect import getmembers
from inspect import isclass
from system.log import Output
class Index(Controller):
    
    def load(self):
        modules = [
            'system.html',
            'system.http',
            'system.log',
        ]
        
        self.library = '<ul>'
        for module in modules:
            mod = import_module(module)
            self.library += '<li>' + module + '</li>'
            self.library += '<ul>'
            for name, obj in getmembers(mod):
                if isclass(obj):
                    if obj.__module__ == module:
                        self.library += '<li><a href="/library/system.http.' + name +'">' + name + '</a></li>'
                        pass
            self.library += '</ul>'
        self.library += '</ul>'   
                        
    def index(self):
        return self.view({
            'username' : 'Syed',
            'password' : 'Hussim',
            'list' : [1,2,3,4,5]
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
            'library' : self.library
        })