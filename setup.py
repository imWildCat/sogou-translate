import os
import io
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
# Import the README and use it as the long-description.
with io.open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

setup(
    name='sogou-translate',
    python_requires='>=3.6.0',
    # If your package is a single module, use this instead of 'packages':
    py_modules=['sogou_translate'],
    version='1.0.1',
    description='The Python wrapper for Sogou Translate API',
    long_description=long_description,
    author='Daohan Chong',
    author_email='wildcat.name@gmail.com',
    url='https://github.com/imWildCat/sogou-translate',
    download_url='https://github.com/imWildCat/sogou-translate/archive/1.0.0.tar.gz',
    keywords=['translate', 'api', 'sougou'],
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    install_requires=[
        'requests',
    ]
)
