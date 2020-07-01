import re
from unidecode import unidecode

from ..utils import translation, squeeze, check_str, check_empty
from .phonetic_algorithm import PhoneticAlgorithm


class Soundex(PhoneticAlgorithm):
    def __init__(self):
        super().__init__()

        self.translations = translation(
            'AEIOUYWHBPFVCSKGJQXZDTLMNR',
            '000000DD111122222222334556'
        )
        self.pad = lambda code: '{}0000'.format(code)[:4]

    def phonetics(self, word):
        check_str(word)
        check_empty(word)

        word = unidecode(word).upper()
        word = re.sub(r'[^A-Z]', r'', word)

        first_letter = word[0]
        tail = ''.join(self.translations[char] for char in word
                       if self.translations[char] != 'D')

        if len(tail):
            if tail[0] == self.translations[first_letter]:
                tail = tail[1:]

        code = squeeze(tail).replace('0', '')
        return self.pad(first_letter + code)
