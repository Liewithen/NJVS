# encoding : utf-8
from __future__ import absolute_import, unicode_literals
from verify.validate import Validate
from NJVS.celery import app

@app.task
def validate_User(username, password):
    user = Validate(username, password)
    if user.judge():
        user.fetch_info()