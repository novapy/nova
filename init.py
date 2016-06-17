from system.web import HttpApplication

class MvcApplication(HttpApplication):
    
    def load(self):
        self.routes.add('/', {'controller' : 'Index', 'action' : 'index'})
        self.routes.add('services.html', {'controller' : 'Index', 'action' : 'services'})
        self.routes.add('^library/system.{lib}', {'controller' : 'Index', 'action' : 'services'})