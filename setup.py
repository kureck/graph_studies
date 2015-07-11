import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


config = {
    'description': 'Graph Route Distance Studies',
    'author': 'Eric Kureck',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'kureck@gmail.com',
    'version': '0.1',
    'install_requires': ['pytest'],
    'packages': ['graph_distance'],
    'scripts': [],
    'name': 'Graph Route distance studies',
    'long_description': read('README.MD')
}

setup(**config)