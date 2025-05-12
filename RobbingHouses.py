
class RobbingHousesClass:

    def __init__(self):
        self.house = [225, 375, 125, 0, 75, 300, 325, 250, 350, 325, 375, 125, 100, 300, 250, 325, 275, 200, 300, 325]


    def max_loot(self):

        max_mon = [0] * (len(self.house))

        max_mon[0] = self.house[0]
        max_mon[1] = max(self.house[0],self.house[1])

        for i in range (2, len(self.house)):

            max_mon[i] = max((self.house[i]+max_mon[i-2]),max_mon[i-1])

        maxloot = max_mon[len(max_mon)-1]
        houses = []

        i = len(self.house)-1

        while i>=0:

            if i == 0  or max_mon[i] == max_mon[i-2]+self.house[i]:

                houses.append(i)
                i -= 2

            else:
                i-=1

        return maxloot,houses







if __name__ == "__main__":

    rob = RobbingHousesClass()
    print(rob.max_loot())




