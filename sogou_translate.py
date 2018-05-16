import requests
import hashlib
import json
import random
from enum import Enum

ERROR_DICT = {
    '1001': 'Translate API: Unsupported language type',
    '1002': 'Translate API: Text too long',
    '1003': 'Translate API: Invalid PID',
    '1004': 'Translate API: Trial PID limit reached',
    '1005': 'Translate API: PID traffic too high',
    '1006': 'Translate API: Insufficient balance',
    '1007': 'Translate API: Random number does not exist',
    '1008': 'Translate API: Signature does not exist',
    '1009': 'Translate API: The signature is incorrect',
    '10010': 'Translate API: Text does not exist',
    '1050': 'Translate API: Internal server error',
}


class SogouTranslateException(Exception):
    def __init__(self, message):

        super().__init__(message)


def _error_code_to_exception(code: str) -> SogouTranslateException:
    return SogouTranslateException(ERROR_DICT[code])


class SogouLanguages(Enum):
    AR = 'ar'  # Arabic
    ET = 'et'  # Estonian
    BG = 'bg'  # Bulgarian
    PL = 'pl'  # Polish
    KO = 'ko'  # Korean
    BS_LATN = 'bs-Latn'  # Bosnian (Latin)
    FA = 'fa'  # Persian
    MWW = 'mww'  # Hmong Daw
    DA = 'da'  # Danish
    DE = 'de'  # German
    RU = 'ru'  # Russian
    FR = 'fr'  # French
    FI = 'fi'  # Finnish
    TLH_QAAK = 'tlh-Qaak'  # Klingon (pIqaD)
    TLH = 'tlh'  # Klingon
    HR = 'hr'  # Croatian
    OTQ = 'otq'  # Querétaro Otomi
    CA = 'ca'  # Catalan
    CS = 'cs'  # Czech
    RO = 'ro'  # Romanian
    LV = 'lv'  # Latvian
    HT = 'ht'  # Haitian Creole
    LT = 'lt'  # Lithuanian
    NL = 'nl'  # Dutch
    MS = 'ms'  # Malay
    MT = 'mt'  # Maltese
    PT = 'pt'  # Portuguese
    JA = 'ja'  # Japanese
    SL = 'sl'  # Slovenian
    TH = 'th'  # Thai
    TR = 'tr'  # Turkish
    SR_LATN = 'sr-Latn'  # Serbian (Latin)
    SR_CYRL = 'sr-Cyrl'  # Serbian (Cyrillic)
    SK = 'sk'  # Slovak
    SW = 'sw'  # Kiswahili
    AF = 'af'  # South African Common Dutch
    NO = 'no'  # Norwegian
    EN = 'en'  # English
    ES = 'es'  # Spanish
    UK = 'uk'  # Ukrainian
    UR = 'ur'  # Urdu
    EL = 'el'  # Greek
    HU = 'hu'  # Hungarian
    CY = 'cy'  # Welsh
    YUA = 'yua'  # Yucatec Maya
    HE = 'he'  # Hebrew
    ZH_CHS = 'zh-CHS'  # Chinese Simplified
    IT = 'it'  # Italian
    HI = 'hi'  # Hindi
    ID = 'id'  # Indonesian
    ZH_CHT = 'zh-CHT'  # Chinese Traditional
    VI = 'vi'  # Vietnamese
    SV = 'sv'  # Swedish
    YUE = 'yue'  # Cantonese
    FJ = 'fj'  # fijian
    FIL = 'fil'  # Filipino
    SM = 'sm'  # Samoan language
    TO = 'to'  # lea fakatonga
    TY = 'ty'  # Tahiti language
    MG = 'mg'  # Malagasy language
    BN = 'bn'  # Bengali


class SogouTranslate:

    SOGOU_API_URL = 'https://fanyi.sogou.com/reventondc/api/sogouTranslate'

    def __init__(self, pid: str, secret_key: str):
        """Initialize SogouTranslate

        Arguments:
            pid {str} -- pid for this service
            secret_key {str} -- secret key for this server

        Raises:
            SogouTranslateException -- while exeception occurs calling this service, detailed exception message will be provided.
        """

        if (not pid) or (not secret_key):
            raise SogouTranslateException('pid or secret key cannot be empty')

        self.pid = pid
        self.secret_key = secret_key

    def _generate_salt(self) -> str:
        """Generate salt string

        Returns:
            str -- the salt string
        """

        return hashlib.sha256(str(random.getrandbits(256)).encode('utf-8')).hexdigest()[:19]

    def _compute_sign(self, source_text: str, salt: str) -> str:
        """Compute the sign string according to Sogou's requirement (https://deepi.sogou.com/docs/fanyiDoc)

        Arguments:
            source_text {str} -- The text to be translated
            salt {str} -- the salt string

        Returns:
            [str] -- The sign string
        """

        text = self.pid + source_text + salt + self.secret_key
        return hashlib.md5(text.encode('utf-8')).hexdigest()

    def _generate_data(self, source_text: str, from_language: SogouLanguages,
                       to_language: SogouLanguages):
        """Generate the data for requesting the translating service

        Arguments:
            source_text {str} -- the text to be translated
            from_language {SogouLanguages} -- the language type of source_text
            to_language {SogouLanguages} -- the language for translation

        Returns:
            dict -- a dictionary containing the data to be posted to Sogou's API server
        """

        salt = self._generate_salt()
        data = {
            'q': source_text,  # text
            'from': from_language.value,  # from language
            'to': to_language.value,  # to language
            'pid': self.pid,  # pid
            'salt': salt,  # salt
            'sign': self._compute_sign(source_text, salt),  # sign
            'charset': 'utf-8',  # charset
            #     'callback': '', # optional for CORs
        }
        return data

    def translate(self, source_text: str, from_language: SogouLanguages,
                  to_language: SogouLanguages) -> str:
        """The translate API

        Arguments:
            source_text {str} -- the text to be translated
            from_language {SogouLanguages} -- the source language type
            to_language {SogouLanguages} -- the target lanaguage type

        Raises:
            SogouTranslateException -- while exeception occurs calling this service, detailed exception message will be provided

        Returns:
            [str] -- the translated text
        """
        if not source_text:
            raise SogouTranslateException('Source text does not exist')

        data = self._generate_data(
            source_text, from_language, to_language
        )
        res = requests.post(self.SOGOU_API_URL, data=data)

        if not res.ok:
            raise SogouTranslateException(
                'Translation request is not successful'
            )

        json_res = json.loads(res.text)

        error_code = json_res['errorCode']
        if error_code != '0':
            raise _error_code_to_exception(error_code)

        return json_res['translation']
