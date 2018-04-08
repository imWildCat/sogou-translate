from setuptools import setup

setup(
    name='sogou-translate',
    python_requires='>=3.6.0',
    # If your package is a single module, use this instead of 'packages':
    py_modules=['sogou_translate'],
    version='0.1',
    description='The Python client for Sogou Translate Service',
    author='Daohan Chong',
    author_email='wildcat.name@gmail.com',
    url='https://github.com/imWildCat/sogou-translate',
    download_url='https://github.com/imWildCat/sogou-translate/archive/0.1.tar.gz',
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
