from .base import *
try:
    from .local import *
except ImportError:
    import warnings
    warnings.warn('Use "settings/local.py" to override settings')
