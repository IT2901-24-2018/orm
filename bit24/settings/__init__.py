from bit24.settings.base import *

try:
    from bit24.settings.local import *
except ImportError as e:
    # No local settings file found.
    # You can still override using environment variables.
    pass
