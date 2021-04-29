from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from app.auth import login_required
from .auth import oidc

bp = Blueprint('index', __name__)


@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/private')
@oidc.require_login
def hello():

	user = oidc.user_getfield("preferred_username")
	access_token = oidc.get_access_token()


	return render_template('private.html', user=user, access_token=access_token)