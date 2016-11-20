# POC Notes

The POC was also documented here: https://pythonicexplorer.wordpress.com/2016/11/20/featured-content/

## Scenario

I recently wondered if it was possible to allow to expose “services” in a more dynamic way. My idea was to provide a location (directory) and then any class that was found in Python code that implemented a specific base class should be made available dynamically. I am also working toward a factory pattern of sorts where by all implementations of a certain base class could be made available through a simple interface.

## Setup

The base class is defined in `test/definitions/defs.py` and contains one base class `Person`.

The code that will attempt to load all implementations of the base class is in `test/service_catalog.py`.

## Testing the example

Try the following:

* Clone the repository somewhere on your machine
* Then run the following:


	$ cd python_poc_stuff/code/selective_class_loading/poc001
	$ python
	Python 3.5.2 (default, Sep 10 2016, 08:21:44)
	[GCC 5.4.0 20160609] on linux
	Type "help", "copyright", "credits" or "license" for more information.
	>>> from test.service_catalog import load_service, SERVICES
	>>> load_service('/home/nicc777/git/python_poc_stuff/code/selective_class_loading/poc001/services/')
	Evaluating dir "/home/nicc777/git/python_poc_stuff/code/selective_class_loading/poc001/services"
	Adding "/home/nicc777/git/python_poc_stuff/code/selective_class_loading/poc001/services" to import path
	Scanning file: /home/nicc777/git/python_poc_stuff/code/selective_class_loading/poc001/services/service_collection_01.py
	  FOUND an implementation of "Person": Man
	  FOUND an implementation of "Person": Woman
	Imported module "service_collection_01"
	>>> SERVICES
	{'Man': <class 'service_collection_01.Man'>, 'Woman': <class 'service_collection_01.Woman'>}
	>>> m = SERVICES['Man']('Pete')
	>>> m.name
	'Pete'
	>>> m.age()
	Always young at heart
	>>> m.is_alive
	True
	>>> m.die()
	>>> m.is_alive
	False

And that's it for now...
