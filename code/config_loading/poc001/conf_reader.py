import sys, os, importlib, traceback

home_dir = os.path.expanduser('~')
conf_file = os.environ.get('APP_CONF_FILE','{}/app_conf_file.py'.format(home_dir))

sys.path.append(os.path.dirname(conf_file))

DEFAULTS = {
    'SERVICE_DIR': '{}/services'.format(home_dir),
    'LOG_DIR': '{}/log'.format(home_dir),
}

CONFIG = None

if os.path.isfile(conf_file):
    print('conf_file "{}" exists - import deferred'.format(conf_file))
else:
    print('conf_file "{}" does not exists - creating one with defaults'.format(conf_file))
    try:
        f = open(conf_file, 'w')
        f.write('import os\n\n')
        for key, value in DEFAULTS.items():
            f.write('{} = os.environ.get(\'{}\', \'{}\')\n'.format(key, key.upper(), value))
        f.close()
        print('Created config file "{}"'.format(conf_file))
    except:
        print('Could not create config file: '.format(traceback.format_exc()))

if os.path.isfile(conf_file):
    print('importing config from "{}"'.format(conf_file))
    try:
        imp_module = os.path.splitext(os.path.basename(conf_file))[0]
        CONFIG = importlib.import_module(imp_module, package=None)
    except:
        print('Nasty error: {}'.format(traceback.format_exc()))
else:
    print('Failed to import anything')
    exit()

if __name__ == '__main__':
    print('service directory : {}'.format(CONFIG.SERVICE_DIR))
    print('log directory     : {}'.format(CONFIG.LOG_DIR))
