from os import path
from system.log import Output
import sys

class Lexer():
    
    def __init__(self, string):
        keywords = ['include']
        self.tokens = []
        token = '';
        codeBlock = False
        count = len(string)
        i = 0
        
        while i < count:
            cc = string[i]
            try:
                nc = string[i+1]
            except:
                nc = ''
                
            if token.strip() in keywords:
                self.tokens.append({ 'type' : 'FUNC', 'token' : token[1:].strip() })
                token = ""
                continue
  
            if cc == "{" and nc == "%" and codeBlock == False:
                self.tokens.append({ 'type' : 'HTML', 'token' : token })
                token = ""
                codeBlock = True
                i+=2
                continue
                
            if cc == "%" and nc == "}" and codeBlock == True:
                self.tokens.append({ 'type' : 'CODE', 'token' : token[1:].strip() })
                token = ""
                codeBlock = False
                i+=2
                continue
            
            token = token + cc
            i+=1

        self.tokens.append({ 'type' : 'HTML', 'token' : token })
        
    def getTokens(self):
        return self.tokens
        
class Compiler():
    
    def compile(rootPath, tokens, data):
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
                if token['token'].find('.') > -1:
                    pass
                else:
                    varName = token['token']
                    if varName in data:
                        val = data[varName]
                        
                        if isinstance(val, str):
                            output += val
                            
                        if isinstance(val, list):
                            output += str(val)
                    #Output.flush(token)
                    #sys.exit()
                
        #Output.flush(tokens)
        #sys.exit()
        return output
        