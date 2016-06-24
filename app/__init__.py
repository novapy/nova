from system.web import HttpApplication

class MvcApplication(HttpApplication):
    
    def load(self):
        self.routes.add('/', {'controller' : 'Index', 'action' : 'index'})
        ##self.routes.add('download', {'controller' : 'Index', 'action' : 'download'})
        self.routes.add('^library/system.{lib}', {'controller' : 'Index', 'action' : 'library'})