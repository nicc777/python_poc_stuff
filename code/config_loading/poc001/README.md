# POC Notes

This is a short experiment to load configuration from a dynamically provided Python source file.

## Scenario

The idea is to define the configuration in Python, which give us other options. I like the idea of getting settings, especially things like passwords, from environment variables and therefore the configuration needs to cater for such scenarios, yet offer logical defaults.

## Setup

Se some environment variables for testing:

	$ export LOG_DIR=/var/log/myapp
	$ export SERVICE_DIR=/tmp/test

And that's it. The configuration will use the environment variable's values or the default.

## Testing the example

Run the script:

	$ python conf_reader.py
	conf_file "/home/user/app_conf_file.py" does not exists - creating one with defaults
	Created config file "/home/user/app_conf_file.py"
	importing config from "/home/user/app_conf_file.py"
	service directory : /tmp/test
	log directory     : /var/log/myapp

As can be seen from the output, the script used the environment variables. The configuration file contains the following:

	$ cat /home/user/app_conf_file.py
	import os
	
	SERVICE_DIR = os.environ.get('SERVICE_DIR', '/home/user/services')
	LOG_DIR = os.environ.get('LOG_DIR', '/home/user/log')

Run another test by deleting one of the environment variables:

	$ unset LOG_DIR
	$ python conf_reader.py
	conf_file "/home/user/app_conf_file.py" exists - import deferred
	importing config from "/home/user/app_conf_file.py"
	service directory : /tmp/test
	log directory     : /home/user/log

As can be seen, the default value for LOG_DIR is now used.
