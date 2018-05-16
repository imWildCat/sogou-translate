import pytest
import os
from sogou_translate import SogouTranslate, SogouLanguages, \
    SogouTranslateException
import hashlib


# Demo keys from: http://deepi.sogou.com/docs/fanyiQa
# TODO: Use mock for testing
SOGOU_PID = os.getenv('SOGOU_PID', default='debc40e19e8f3675ee1f93b480ec3104')
SOGOU_SKEY = os.getenv(
    'SOGOU_SKEY', default='51b3cc5bb7d97d0c02e8bbd8fbbd84cd')


@pytest.fixture
def translate_instance():
    return SogouTranslate(SOGOU_PID, SOGOU_SKEY)


def test_empty_pid():
    with pytest.raises(SogouTranslateException):
        SogouTranslate('', 'foo')


def test_none_pid():
    with pytest.raises(SogouTranslateException):
        SogouTranslate(None, 'foo')


def test_empty_secret_key():
    with pytest.raises(SogouTranslateException):
        SogouTranslate('foo', '')


def test_none_secret_key():
    with pytest.raises(SogouTranslateException):
        SogouTranslate('foo', None)


def test_generate_salt():
    trans = translate_instance()
    salt = trans._generate_salt()
    assert len(salt) == 19


def test_compute_sign():
    trans = translate_instance()
    salt = trans._generate_salt()
    source_text = 'Hello, world!'
    sign = trans._compute_sign(source_text, salt)

    exptected_raw = SOGOU_PID + source_text + salt + SOGOU_SKEY
    expected = hashlib.md5(exptected_raw.encode('utf-8')).hexdigest()

    assert expected == sign


def test_generate_data():
    trans = translate_instance()
    source_text = 'Hello, world!'

    data = trans._generate_data(source_text,
                                from_language=SogouLanguages.EN,
                                to_language=SogouLanguages.ZH_CHS)
    assert data['q'] == source_text
    assert data['charset'] == 'utf-8'
    assert data['from'] is SogouLanguages.EN.value
    assert data['to'] is SogouLanguages.ZH_CHS.value
    assert data['pid'] == SOGOU_PID


def test_translate():
    trans = translate_instance()
    source_text = 'Hello, world!'

    response_text = \
        trans.translate(source_text, SogouLanguages.EN, SogouLanguages.ZH_CHS)
    assert '你好' in response_text
    assert '世界' in response_text


def test_bad_key():
    trans = SogouTranslate('bad_pid', 'bad_secret')
    with pytest.raises(SogouTranslateException):
        trans.translate('Foo bar', SogouLanguages.EN, SogouLanguages.FR)


def test_empty_source_text():
    trans = translate_instance()
    with pytest.raises(SogouTranslateException):
        trans.translate('', SogouLanguages.EN, SogouLanguages.ZH_CHS)
