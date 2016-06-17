from collections import Sequence

class RouteCollection(Sequence):
    
    def __init__(self):
        self.collection = []
        
    def add(self, name, params):
        self.collection.append(Route(name, params))
        
    def __getitem__(self, index):
        return self.collection[index]
    
    def __len__(self):
        return len(self.collection)
    
    def toArray(self):
        return self.collection
    
    
class Route():
    
    def __init__(self, route, params):
        self.route = route
        self.params = params
        self.handler = RouteHandler()
        
    def setHttpRequest(self, httpRequest):
        self.httpRequest = httpRequest
        
    def getRoute(self):
        return self.route
    
    def getParams(self):
        return self.params
    
    def execute(self, httpRequest):
        return self.handler.execute(httpRequest, self.route, self.params)
        
        
class RouteHandler():
    
    def execute(self, httpRequest, route, params):
        uri = httpRequest.getUri();

        if route[0:1] == '^' and len(uri) > 0:

            route = route[1:]
            
            token = ""
            tokens = []
            placeHolders = []

            for ch in route:
                if ch =="{":
                    tokens.append(token)
                    token = ''
                    continue
                    
                if ch =="}":
                    placeHolders.append(token)
                    token = ''
                    continue

                token = token + ch
                    
            tokens.append(token)
            
            for token in tokens:
                uri = uri.replace(token, '#')
        
            replaceTokens = list(filter(None,uri.split('#')))
            
            for idx, holder in enumerate(placeHolders):
                route = route.replace('{'+ holder + '}', replaceTokens[idx])
                params[holder] = replaceTokens[idx]

        if httpRequest.getUri() == route:
            return params
        elif len(httpRequest.getUri()) == 0 and route == '/':
            return params
        else:
            return {}
        
        