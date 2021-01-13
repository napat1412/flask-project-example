from flask import Blueprint
from app import oidc
from flask import g

api_user = Blueprint('api_user', __name__)

""" Backend for api that verify OIDC access_token """
@api_user.route("/api")
@oidc.accept_token(require_token=True, render_errors=True)
def oidc_token_detail():
  print("oidc-token details")
  user = {}
  user['preferred_username'] = g.oidc_token_info['preferred_username']
  user['name'] = g.oidc_token_info['name']
  user['email'] = g.oidc_token_info['email']
  user['sub'] = g.oidc_token_info['sub']
  user['realm_access'] = g.oidc_token_info['realm_access']
  
  print(g.oidc_token_info['preferred_username'])
  print(g.oidc_token_info['name'])
  print(g.oidc_token_info['email'])
  print(g.oidc_token_info['sub'])
  print(g.oidc_token_info['realm_access'])
  return user


""" Frontend: OIDC User Login/Logout """
@api_user.route('/')
def hello_world():
    if oidc.user_loggedin:
        return ('Hello, %s, <a href="/oidc/private">See private</a> '
                '<a href="/oidc/logout">Log out</a>') % \
            oidc.user_getfield('preferred_username')
    else:
        return 'Welcome anonymous, <a href="/oidc/private">Log in</a>'


@api_user.route('/private')
@oidc.require_login
def hello_me():
    """Example for protected endpoint that extracts private information from the OpenID Connect id_token.
       Uses the accompanied access_token to access a backend service.
    """

    info = oidc.user_getinfo(['preferred_username', 'email', 'sub'])

    username = info.get('preferred_username')
    email = info.get('email')
    user_id = info.get('sub')

    if user_id in oidc.credentials_store:
        try:
            from oauth2client.client import OAuth2Credentials
            access_token = OAuth2Credentials.from_json(oidc.credentials_store[user_id]).access_token
            print('access_token=<%s>' % access_token)
            headers = {'Authorization': 'Bearer %s' % (access_token)}
            # YOLO
            greeting = requests.get('http://localhost:8080/greeting', headers=headers).text
        except:
            print("Could not access greeting-service")
            greeting = "Hello %s" % username
    

    return ("""%s your email is %s and your user_id is %s!
               <ul>
                 <li><a href="/oidc/">Home</a></li>                 
                </ul>""" %
            (greeting, email, user_id))

@api_user.route('/logout')
def logout():
    """Performs local logout by removing the session cookie."""

    oidc.logout()
    return 'Hi, you have been logged out! <a href="/oidc/">Return</a>'