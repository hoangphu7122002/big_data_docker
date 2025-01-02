import os
import pwd
from nativeauthenticator import NativeAuthenticator

c = get_config()
from jupyterhub.auth import LocalAuthenticator
from nativeauthenticator import NativeAuthenticator

class LocalNativeAuthenticator(NativeAuthenticator, LocalAuthenticator):
    pass

c.JupyterHub.authenticator_class = LocalNativeAuthenticator
c.Authenticator.open_signup = False
c.Authenticator.admin_users = {'phundh'}
c.LocalAuthenticator.create_system_users = True
c.Authenticator.allow_all = False
c.Authenticator.allow_existing_users = True
c.Authenticator.allowed_users = {'phundh', 'bob', 'alice', 'minhnh'}
c.Spawner.default_url = '/lab'

c.JupyterHub.shutdown_on_logout = True
c.JupyterHub.logout_redirect_url = '/'
c.Spawner.enable_terminal = True