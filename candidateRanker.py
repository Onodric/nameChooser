import candidateGetter as cg
import secrets


class CandidateRanker:
    """

    """
    def __init__(self):
        """

        """
        self.candidates = dict()
        self.final_candidates = dict()
        self.final_finals = dict()
        self.cg = cg.CandidateMaker()

    def get_candidates(self, n, l):
        """

        :param n:
        :param l:
        :return:
        """
        self.candidates = self.cg.do_it_up(l, n)

    def rank_one(self, iterations):
        """

        :param iterations:
        :return:
        """
        self.get_candidates(100, 15)
        for count in range(iterations):
            print("rank_one count: {}".format(count))
            for candidate in self.candidates.keys():
                ranking = secrets.randbelow(len(
                    self.candidates))
                if candidate in self.final_candidates:
                    self.final_candidates[candidate] += ranking
                else:
                    self.final_candidates[candidate] = ranking

    def top_candidates(self, low_rank):
        """

        :param low_rank:
        :return:
        """
        final_rankings = dict()
        for k in sorted(self.final_candidates,
                        key=self.final_candidates.get, reverse=True)[:low_rank]:
            final_rankings[k] = self.final_candidates[k]
        print("Top_Candidates dict: {}".format(final_rankings))
        self.final_candidates = {}
        return final_rankings

    def do_that_a_lot(self, iterations):
        """

        :param iterations:
        :return:
        """
        for i in range(iterations):
            self.rank_one(50)
            # print("do-that_a_lot got a list: {}".format(self.final_candidates))
            top_ten = self.top_candidates(10)
            print("this is the top ten #{}: {}".format(i, top_ten))
            for top, rank in top_ten.items():
                if top in self.final_finals:
                    self.final_finals[top] += rank
                else:
                    self.final_finals[top] = rank
            if len(self.final_finals) >= 100:
                temp_tops = self.top_candidates(50)
                for top, rank in temp_tops.items():
                    self.final_finals[top] += rank
        print(self.final_finals)
        self.final_candidates = self.final_finals
        print("Final top 25: ")
        self.top_candidates(25)


if __name__ == "__main__":
    cr = CandidateRanker()
    cr.do_that_a_lot(10)
