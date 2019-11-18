from flask import render_template, Blueprint, redirect, session

import school_schedule_app.infrastructure.cookie_auth as cookie_auth


blueprint = Blueprint('account', __name__, template_folder='templates')


@blueprint.route('/account', methods=['GET'])
def index_get():

    return render_template('account/index.html')


@blueprint.route('/account', methods=['POST'])
def index_post():

    return redirect('/account')


# LOGIN

@blueprint.route('/account/login', methods=['GET'])
def login_get():

    return render_template('account/login.html', vm=None)


@blueprint.route('/account/login', methods=['POST'])
def login_post():
    print("Logged!")
    return redirect("/")
    # if not user:
    #     return render_template('account/login.html', vm=vm.to_dict())
    # else:
    #     # Create cookie
    #     session.clear()
    #     resp = redirect('/')
    #     cookie_auth.set_auth(resp, user.id)
    #
    #     return resp


# REGISTER
@blueprint.route('/account/register', methods=['GET'])
def register_get():
    return render_template('account/register.html', vm=None)


@blueprint.route('/account/register', methods=['POST'])
def register_post():

    return redirect('/account/login')


# FORGOT PASSWORD
@blueprint.route('/account/forgot_password', methods=['GET'])
def forgot_password_get():
    return render_template('account/forgot_password.html')


@blueprint.route('/account/forgot_password', methods=['POST'])
def forgot_password_post():
    return render_template('account/forgot_password.html')

# LOGOUT

@blueprint.route('/account/logout')
def logout():
    resp = redirect('/account/login')
    cookie_auth.logout(resp)

    return resp