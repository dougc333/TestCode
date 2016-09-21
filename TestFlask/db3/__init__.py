from flask import Flask


app = Flask(__name__)
from db3 import views
