from os import path
from html import escape
from html import unescape

class Lexer():
    
    def __init__(self, string):
        
        token = '';
        codeBlock = False
        count = len(string)
        i = 0
        lineCount = 1;
        self.tokens = []
        
        while i < count:
            cc = string[i]
            try:
                nc = string[i+1]
            except:
                nc = ''

            if token.strip() == 'include':
                self.tokens.append({ 'type' : 'FUNC', 'token' : token[1:].strip() , 'line' : lineCount})
                token = ""
                continue
  
            if cc == "{" and nc == "%" and codeBlock == False:
                self.tokens.append({ 'type' : 'HTML', 'token' : token })
                token = ""
                codeBlock = True
                i+=2
                continue
                
            if cc == "%" and nc == "}" and codeBlock == True:
                self.tokens.append({ 'type' : 'CODE', 'token' : token[1:].strip(), 'line' : lineCount})
                token = ""
                codeBlock = False
                i+=2
                continue
            
            token = token + cc
            i+=1
            
            if cc == "\n":
                lineCount +=1

        self.tokens.append({ 'type' : 'HTML', 'token' : token , 'line' : lineCount})
        
    def getTokens(self):
        return self.tokens
        
class Compiler():
    
    def compile(rootPath, tokens, data = {}):

        output = ""
        for i, token in enumerate(tokens):
            if token['type'] == 'HTML':
                output += token['token']
                
            elif token['type'] == 'FUNC':
                if token['token'].lower() == 'include':
                    nextToken = tokens[i+1];
                    if nextToken['type'] == 'CODE':
                        file = rootPath + nextToken['token'][1:-1]
                        if path.isfile(file):
                            f = open(file, 'r');
                            lexer = Lexer(f.read())
                            output += Compiler.compile(rootPath, lexer.getTokens(), data)
                        else:
                            raise Exception("Include file not found")
                        
            elif token['type'] == 'CODE':
                value = ''
                
                if token['token'].find('.') > -1:
                    segments = token['token'].split('.')

                    if segments[0] in data:
                        if type(data[segments[0]]).__name__ == 'object':
                            objName = segments[0]
                            objProp = segments[1]
                            obj = data[objName]
                            del segments[0]
                            del segments[1]

                            if hasattr(obj, objProp):
                                value = escape(getattr(obj, objProp))

                        if type(data[segments[0]]).__name__ == 'str':
                            value  = escape(data[segments[0]])
                            del segments[0]

                    if len(segments) > 0:
                        functions = Functions(value)

                        for segment in segments:
                            funcName = segment[:segment.find('(')]
                            functions = Functions(value)
                            if hasattr(functions, funcName):
                                func = getattr(functions, funcName)
                                value = func()
                else:
                    value = data[token['token']]
                output += value
        return output

class Functions():
    
    def __init__(self, value):
        self.value = value
        
    def upper(self):
        return self.value.upper()
    
    def lower(self):
        return self.value.lower()
    
    def strip(self):
        return self.value.strip()
        
    def raw(self):
        return unescape(self.value)