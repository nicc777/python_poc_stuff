import os, sys, traceback, importlib, inspect
from test.definitions.defs import Person

SERVICES = {}


def load_service(services_dir):
	if os.path.isdir(services_dir):
		dirs_seen = []
		for root, dirs, files in os.walk(services_dir, topdown=False):
			for name in files:
				file_name = os.path.join(root, name)
				if 'pycache' not in file_name and '__init__' not in file_name:
					dir_name = os.path.dirname(file_name)
					print('Evaluating dir "{}"'.format(dir_name))
					if not dir_name in dirs_seen:
						print('Adding "{}" to import path'.format(dir_name))
						dirs_seen.append(dir_name)
						sys.path.append(dir_name)
					print('Scanning file: {}'.format(file_name))
					try:
						imp_module = os.path.splitext(os.path.basename(file_name))[0]
						new_module = importlib.import_module(imp_module, package=None)	
						for class_name in dir(new_module):
							if class_name != 'Person':
								if isinstance(getattr(new_module, class_name), type):
									class_def = getattr(new_module, class_name)
									if issubclass(class_def, Person):
										print('\tFOUND an implementation of "Person": {}'.format(class_name))
										SERVICES[class_name] = class_def
						print('Imported module "{}"'.format(imp_module))
					except:
						print('Failed to load module "{}" :: {}'.format(imp_module,traceback.format_exc()))
						
