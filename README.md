Sogou-Translate
===

The Python wrapper for [Sogou Translate API](http://deepi.sogou.com/docs/fanyiDoc). Only **Python 3.6** is supported.

## Get started
You could install this library using `pip`:

```shell
pip install sogou-translate
```

Note: You might have to [apply for the keys](http://deepi.sogou.com/docs/fanyiQa) in order to use the service. If you wish to have a brief demo of this service, you could use the demo keys mentioned in the related web pages.

## Example usage
```python
from sogou_translate import SogouTranslate, SogouLanguages

sogou_translate = SogouTranslate('[Your pid]', '[Your secret key]')

en_text = 'Hello, world!'
zh_text = sogou_translate.translate(en_text, from_language=SogouLanguages.EN, to_language=SogouLanguages.ZH_CHS)
print(zh_text) # '你好，世界！'
```

## License

The code is licensed under DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE. For more details, read the [LICENSE](./LICENSE) file.