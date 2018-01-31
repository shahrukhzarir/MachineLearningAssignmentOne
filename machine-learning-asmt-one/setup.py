try:
	from setuptools import setup, find_packages
except ImportError:
	from distutils.core import setup

config = {
	'description': 'package description',
	'author': 'Shahrukh Zarir',
	'author_email': 'shahrukh.zarir@uoit.net',
	'version': '0.0.1',
	'packages': find_packages(),
	'name': 'package_name'
}
setup(**config)
