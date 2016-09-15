from flask import Flask

#template_folder='hello_templates'
app = Flask('__name__',root_path='hellotemplates')
from hellotemplates import view

