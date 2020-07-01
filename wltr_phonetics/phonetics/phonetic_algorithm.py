from ..distance_metrics import levenshtein_distance, hamming_distance
from ..exceptions import DistanceMetricError


class PhoneticAlgorithm:
    def __init__(self):
        self.distances = {
            'levenshtein': levenshtein_distance,
            'hamming': hamming_distance,
        }

    def phonetics(self, word):
        pass

    def sounds_like(self, word1, word2):
        return self.phonetics(word1) == self.phonetics(word2)

    def distance(self, word1, word2, metric='levenshtein'):
        if metric in self.distances:
            distance_func = self.distances[metric]
            return distance_func(self.phonetics(word1), self.phonetics(word2))
        else:
            raise DistanceMetricError('Distance metric not supported! Choose from levenshtein, hamming.')
