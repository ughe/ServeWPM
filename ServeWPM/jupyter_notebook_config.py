# Imports
import os

#------------------------------------------------------------------------------
# JupyterApp(Application) configuration
#------------------------------------------------------------------------------

c.NotebookApp.allow_root=True

## Hashed password to use for web authentication.
#  
#  To generate, type in a python/IPython shell:
#  
#    from notebook.auth import passwd; passwd()
#  
#  The string should be of the form type:salt:hashed-password.
c.NotebookApp.password = str(os.environ['JUPYTER_PASSWORD_HASH'])

## The IP address the notebook server will listen on.
c.NotebookApp.ip = str(os.environ['HOST_IP'])

## The port the notebook server will listen on.
c.NotebookApp.port = 80

## Base class for Jupyter applications

## Answer yes to any prompts.
#c.JupyterApp.answer_yes = False

## Full path of a config file.
#c.JupyterApp.config_file = u''

## Specify a config file to load.
#c.JupyterApp.config_file_name = u''

#------------------------------------------------------------------------------
# NotebookApp(JupyterApp) configuration
#------------------------------------------------------------------------------

## Set the Access-Control-Allow-Credentials: true header
#c.NotebookApp.allow_credentials = False

## Set the Access-Control-Allow-Origin header
#  
#  Use '*' to allow any origin to access your server.
#  
#  Takes precedence over allow_origin_pat.
#c.NotebookApp.allow_origin = ''

## The base URL for the notebook server.
#  
#  Leading and trailing slashes can be omitted, and will automatically be added.
#c.NotebookApp.base_url = '/'

## The full path to an SSL/TLS certificate file.
#c.NotebookApp.certfile = u''

## The full path to a certificate authority certificate for SSL/TLS client
#  authentication.
#c.NotebookApp.client_ca = u''

## Extra keyword arguments to pass to `set_secure_cookie`. See tornado's
#  set_secure_cookie docs for details.
#c.NotebookApp.cookie_options = {}

## The random bytes used to secure cookies. By default this is a new random
#  number every time you start the Notebook. Set it to a value in a config file
#  to enable logins to persist across server sessions.
#  
#  Note: Cookie secrets should be kept private, do not share config files with
#  cookie_secret stored in plaintext (you can read the value from a file).
#c.NotebookApp.cookie_secret = ''

## The file where the cookie secret is stored.
#c.NotebookApp.cookie_secret_file = u''

## The default URL to redirect to from `/`
#c.NotebookApp.default_url = '/tree'

## extra paths to look for Javascript notebook extensions
#c.NotebookApp.extra_nbextensions_path = []

## Extra paths to search for serving static files.
#  
#  This allows adding javascript/css to be available from the notebook server
#  machine, or overriding individual files in the IPython
#c.NotebookApp.extra_static_paths = []

## (bytes/sec) Maximum rate at which stream output can be sent on iopub before
#  they are limited.
#c.NotebookApp.iopub_data_rate_limit = 1000000

## (msgs/sec) Maximum rate at which messages can be sent on iopub before they are
#  limited.
#c.NotebookApp.iopub_msg_rate_limit = 1000

## The MathJax.js configuration file that is to be used.
#c.NotebookApp.mathjax_config = 'TeX-AMS-MML_HTMLorMML-full,Safe'

## Dict of Python modules to load as notebook server extensions.Entry values can
#  be used to enable and disable the loading ofthe extensions. The extensions
#  will be loaded in alphabetical order.
# c.NotebookApp.nbserver_extensions = {}

## The directory to use for notebooks and kernels.
c.NotebookApp.notebook_dir = str(os.environ['NOTEBOOKS'])

## Whether to open in a browser after starting. The specific browser used is
#  platform dependent and determined by the python standard library `webbrowser`
#  module, unless it is overridden using the --browser (NotebookApp.browser)
#  configuration option.
c.NotebookApp.open_browser = False

## Forces users to use a password for the Notebook server. This is useful in a
#  multi user environment, for instance when everybody in the LAN can access each
#  other's machine through ssh.
#  
#  In such a case, server the notebook server on localhost is not secure since
#  any user can connect to the notebook server via ssh.
#c.NotebookApp.password_required = False

## DISABLED: use %pylab or %matplotlib in the notebook to enable matplotlib.
# c.NotebookApp.pylab = 'disabled'

## Token used for authenticating first-time connections to the server.
#  
#  When no password is enabled, the default is to generate a new, random token.
#  
#  Setting to an empty string disables authentication altogether, which is NOT
#  RECOMMENDED.
#c.NotebookApp.token = '<generated>'

## The base URL for websockets, if it differs from the HTTP server (hint: it
#  almost certainly doesn't).
#  
#  Should be in the form of an HTTP origin: ws[s]://hostname[:port]
#c.NotebookApp.websocket_url = ''

#------------------------------------------------------------------------------
# ConnectionFileMixin(LoggingConfigurable) configuration
#------------------------------------------------------------------------------

## Username for the Session. Default is your system username.
c.Session.username = u'admin'


#------------------------------------------------------------------------------
# ContentsManager(LoggingConfigurable) configuration
#------------------------------------------------------------------------------

## Glob patterns to hide in file and directory listings.
#c.ContentsManager.hide_globs = [u'__pycache__', '*.pyc', '*.pyo', '.DS_Store', '*.so', '*.dylib', '*~']

## Python callable or importstring thereof
#  
#  To be called on a contents model prior to save.
#  
#  This can be used to process the structure, such as removing notebook outputs
#  or other side effects that should not be saved.
#  
#  It will be called as (all arguments passed by keyword)::
#  
#      hook(path=path, model=model, contents_manager=self)
#  
#  - model: the model to be saved. Includes file contents.
#    Modifying this dict will affect the file that is stored.
#  - path: the API path of the save destination
#  - contents_manager: this ContentsManager instance
#c.ContentsManager.pre_save_hook = None

## 
#c.ContentsManager.root_dir = '/'

## The base name used when creating untitled directories.
#c.ContentsManager.untitled_directory = 'Untitled Folder'

## The base name used when creating untitled files.
#c.ContentsManager.untitled_file = 'untitled'

## The base name used when creating untitled notebooks.
#c.ContentsManager.untitled_notebook = 'Untitled'

#------------------------------------------------------------------------------
# FileContentsManager(FileManagerMixin,ContentsManager) configuration
#------------------------------------------------------------------------------

## Python callable or importstring thereof
#  
#  to be called on the path of a file just saved.
#  
#  This can be used to process the file on disk, such as converting the notebook
#  to a script or HTML via nbconvert.
#  
#  It will be called as (all arguments passed by keyword)::
#  
#      hook(os_path=os_path, model=model, contents_manager=instance)
#  
#  - path: the filesystem path to the file just written - model: the model
#  representing the file - contents_manager: this ContentsManager instance
#c.FileContentsManager.post_save_hook = None

## 
#c.FileContentsManager.root_dir = u''

#------------------------------------------------------------------------------
# NotebookNotary(LoggingConfigurable) configuration
#------------------------------------------------------------------------------

## A callable returning the storage backend for notebook signatures. The default
#  uses an SQLite database.
#c.NotebookNotary.store_factory = traitlets.Undefined
