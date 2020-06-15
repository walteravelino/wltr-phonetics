import re
from unidecode import unidecode

from ..utils import squeeze, check_empty, check_str
from .phonetic_algorithm import PhoneticAlgorithm


class MatchingRatingApproach(PhoneticAlgorithm):
    def __init__(self):
        super().__init__()

    def phonetics(self, word):
        check_str(word)
        check_empty(word)

        codex = unidecode(word).upper()
        codex = re.sub(r'[^A-Z]', r'', codex)

        codex = codex[0] + re.sub(r'[AEIOU]', r'', codex[1:])

        codex = squeeze(codex)

        offset = min(3, len(codex) - 3)
        return codex[:3] + codex[len(codex) - offset:offset + len(codex)]
