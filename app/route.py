from app import app, db, oidc

import json
from flask import Flask, g, request, flash, url_for, redirect, render_template

from app.routes.oidc import api_user
app.register_blueprint(api_user, url_prefix='/oidc')

from app.routes.db import api_db
app.register_blueprint(api_db, url_prefix='/db')


@app.route("/")
def about():
  return ("""
          <ul>
            <li><a href="/oidc/">OIDC example</a></li>
            <li><a href="/db/student">Model example</a></li>
          </ul>""")
  #return "All about Flask"