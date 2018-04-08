Sogou-Translate |Build Status| |codecov| |PyPI version|
=======================================================

The Python wrapper for `Sogou Translate
API <http://deepi.sogou.com/docs/fanyiDoc>`__. Only **Python 3.6** is
supported.

.. figure:: https://user-images.githubusercontent.com/2396817/38472358-b1b2aa96-3b76-11e8-85ec-bbd7b47fc3a8.png
   :alt: sogou_translate_logo

   sogou_translate_logo

Get started
-----------

You could install this library using ``pip``:

.. code:: shell

    pip install sogou-translate

Note: You might have to `apply for the
keys <http://deepi.sogou.com/docs/fanyiQa>`__ in order to use the
service. If you wish to have a brief demo of this service, you could use
the demo keys mentioned in the related web pages.

Example usage
-------------

.. code:: python

    from sogou_translate import SogouTranslate, SogouLanguages

    trans = SogouTranslate('[Your pid]', '[Your secret key]')

    en_text = 'Hello, world!'
    zh_text = trans.translate(en_text, from_language=SogouLanguages.EN, to_language=SogouLanguages.ZH_CHS)
    print(zh_text) # '你好，世界！'

License
-------

The code is licensed under DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE.
For more details, read the `LICENSE <./LICENSE>`__ file.

.. |Build Status| image:: https://travis-ci.org/imWildCat/sogou-translate.svg?branch=master
   :target: https://travis-ci.org/imWildCat/sogou-translate
.. |codecov| image:: https://codecov.io/gh/imWildCat/sogou-translate/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/imWildCat/sogou-translate
.. |PyPI version| image:: https://badge.fury.io/py/sogou-translate.svg
   :target: https://badge.fury.io/py/sogou-translate
