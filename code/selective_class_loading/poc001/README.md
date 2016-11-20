# POC Notes

The POC was also documented here: https://pythonicexplorer.wordpress.com/2016/11/20/featured-content/

## Scenario

I recently wondered if it was possible to allow to expose “services” in a more dynamic way. My idea was to provide a location (directory) and then any class that was found in Python code that implemented a specific base class should be made available dynamically. I am also working toward a factory pattern of sorts where by all implementations of a certain base class could be made available through a simple interface.

## Setup

The base class is defined in `test/definitions/defs.py` and contains one base class `Person`.

The code that will attempt to load all implementations of the base class is in `test/service_catalog.py`.
