from flask import Flask

#template_folder='hello_templates'
app = Flask('__name__',root_path='hellotemplates1')
from hellotemplates1 import view

