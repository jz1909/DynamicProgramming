class MakingChangeClass:

    c = [1, 3, 4, 15, 20, 30, 50, 100]

    def __init__(self):
        print(self.make_change(self.c, 133))


    def make_change(self, C, n):

        num_coins = [0]*(n+1)
        num_coins[0] = 0

        for k in range (1,n+1):
            best = None

            for coin in C:
                if k-coin >= 0 and num_coins[k-coin] is not None:

                    candidate =  num_coins[k-coin]+1

                    if best is None or candidate < best:
                        best = candidate

            num_coins[k] = best


        return num_coins[n]



MakingChangeClass()




