from collections import OrderedDict
from system.log import Output
class Element():
    
    def setAttributes(self, attrs = {}):
        self._attrs = attrs
        
    def _renderAttributes(self):
        string = ''
        for idx, key in enumerate(self._attrs):
            string +='{0}="{1}" '.format(key, self._attrs[key]).strip()
        return string
    
    def render(self):
        pass
    
class Table(Element):
    
    def __init__(self):
        self._headers = OrderedDict()
        self._data = []
        
    def addHeader(self, header, text):
        self._headers[header] = text
        
    def addRow(self, data):
        self._data.append(data)
        
    def toArray(self):
        return self._data
    
    def render(self):
        control = ''

        for row in self._data:
            control += '<tr>'
            for header in self._headers:
                control += '<td>' + str(row[header]) + '</td>'
            control += '</tr>'
            
        return '<table ' + self._renderAttributes() + '>' + control + '</table>'
            