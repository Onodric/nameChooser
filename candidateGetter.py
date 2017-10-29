import word_list
import secrets


class CandidateMaker:
    """
    Class to populate a dictionary of candidate words

    ToDo:
        - given constraints, use the word list to gather a list of words

    """
    def __init__(self):
        """
        The constructor for CandidateMaker
        """
        self.word_list = word_list.words
        self.max_index = len(self.word_list) - 1

    def do_it_up(self, longest_word, number_of_candidates):
        """

        :param longest_word:
        :param number_of_candidates:
        :return: a dictionary {candidate: 0}
        """
        candidates = set()
        while len(candidates) < number_of_candidates:
            rand_index = secrets.randbelow(self.max_index)
            candidate = self.word_list[rand_index]
            if len(candidate) <= longest_word:
                candidates.add(candidate)
        candidate_list = list(candidates)
        return dict((el, 0) for el in candidate_list)


if __name__ == "__main__":
    candidate_maker = CandidateMaker()
    candidate_dict = candidate_maker.do_it_up(15, 50)
    print('\n'.join(['{}: {}'.format(candidate, score) for candidate,
                    score in candidate_dict.items()]))
