from setuptools import setup

setup(
    name='sogou-translate',
    packages=['sogou-translate'],
    python_requires='>=3.6.0',
    py_modules=['sogou_translate1'],
    version='0.1',
    description='The Python client for Sogou Translate Service',
    author='Daohan Chong',
    author_email='wildcat.name@gmail.com',
    url='https://github.com/imWildCat/sogou-translate',
    download_url='https://github.com/imWildCat/sogou-translate/archive/0.1.tar.gz',
    keywords=['translate', 'api', 'sougou'],
    classifiers=[],
    install_requires=[
        'requests',
    ]
)
