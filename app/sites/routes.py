from flask import Flask, render_template, Blueprint  

site = Blueprint('site', __name__, template_folder='site_templates')

@site.route('/')
def home():
    return render_template('index.html')

@site.route('/inventory')
def inventory():
    return render_template('inventory.html')