import os


def state_dir():
    '''
    Base directory for app state (settings, cache, logs, completed list).

    Honors XDG_CONFIG_HOME so the app works when installed system-wide
    and launched from any working directory.
    '''
    base = os.environ.get('XDG_CONFIG_HOME') or os.path.join(os.path.expanduser('~'), '.config')
    return os.path.join(base, '1fichier-dl')
