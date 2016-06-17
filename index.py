#!/Python34/python

import sys
import cgitb
import os
sys.dont_write_bytecode = True
cgitb.enable()

from init import MvcApplication

#try:
app = MvcApplication(os.path.dirname(os.path.realpath(__file__)).replace("\\", "/"))
app.load()
app.run()
app.end()
#except Exception as e:
    #app.error(e)
    