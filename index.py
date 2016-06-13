#!/Python34/python

from init import mvc

print("Content-type: text/html")
print("")

app = mvc()
app.load()
app.run()
