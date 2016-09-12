from test import a
#import a

print "asdf"
print "test_list:",a.test_list


from flask import Flask
app = Flask(__name__)
app.config.from_object("a")
