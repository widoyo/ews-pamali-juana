from flask import Blueprint, request, render_template, redirect, url_for, jsonify, flash
from flask_login import login_required, current_user
from flask_wtf.csrf import generate_csrf
from sqlalchemy import extract, and_
from psycopg2 import IntegrityError
import datetime
import calendar

from ews_app import roles_filter
from ews_app.admin import bp


@bp.route('/alert')
@login_required
@roles_filter(roles=['admin', 'pejabat'])
def alert():
    ''' Index alert '''
    return render_template('admin/alert/index.html')
