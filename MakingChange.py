class MakingChangeClass:

    c = [1, 4, 9, 15, 25, 40, 75, 100]

    def __init__(self):
        for i in range (1,201):
            print(self.make_change(self.c,i))




    def make_change(self, C, n):

        num_coins = [0]*(n+1)
        num_coins[0] = 0
        choice = [0]*(n+1)
        choice[0] = 0

        for k in range (1,n+1):
            best = None
            best_coin = None

            for coin in C:
                if k-coin >= 0 and num_coins[k-coin] is not None:

                    candidate =  num_coins[k-coin]+1

                    if best is None or candidate < best:
                        best = candidate
                        best_coin = coin

            num_coins[k] = best
            choice[k] = best_coin


        result_coins = []

        if num_coins[n] is None:
            result_coins = None

        i = n

        while i>0:
            result_coins.append(choice[i])
            i = i-choice[i]

        return num_coins[n], result_coins



MakingChangeClass()




