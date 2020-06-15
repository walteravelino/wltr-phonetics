import re
from unidecode import unidecode

from ..utils import squeeze, translation, check_str, check_empty
from .phonetic_algorithm import PhoneticAlgorithm


class Lein(PhoneticAlgorithm):
    def __init__(self):
        super().__init__()

        self.translations = translation(
            'DTMNLRBFPVCJKGQSXZ',
            '112233444455555555'
        )

        self.pad = lambda code: '{}0000'.format(code)[:4]

    def phonetics(self, word):
        check_str(word)
        check_empty(word)

        word = unidecode(word).upper()
        word = re.sub(r'[^A-Z]\s', r'', word)

        first, code = word[0], word[1:]

        code = re.sub(r'[AEIOUYWH]', r'', code)

        code = squeeze(code)[0: 4]

        code = ''.join(self.translations.get(char, char) for char in code)

        return self.pad(first + code)
