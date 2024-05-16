from .env import *

if DEBUG:
    from .dev import *
else:
    from .prod import *