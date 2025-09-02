import json

# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for, jsonify, send_file, Response, abort

# Import module forms
#from app.main_page_module.p_objects.note_o import N_obj


from wrappers import login_required
from app.pylavor import Pylavor
from app.main_page_module.other import Randoms


from app import app, targets_ram

#import os
import re
import os
import io
import pathlib
from passlib.hash import sha512_crypt
import datetime


# Define the blueprint: 'auth', set its url prefix: app.url/auth
main_page_module = Blueprint('main_page_module', __name__, url_prefix='/')


@app.context_processor
def inject_to_every_page():
    
    return dict(Randoms=Randoms, datetime=datetime, Pylavor=Pylavor)


# Set the route and accepted methods
@main_page_module.route('/', methods=['GET'])
def index():
    return render_template("main_page_module/index.html")


# Set the route and accepted methods
@main_page_module.route('/preview/', methods=['GET'])
def preview():
    return render_template("main_page_module/preview.html")


