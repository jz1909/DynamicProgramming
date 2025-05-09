class RoadTripClass:


    def __init__(self):
        self.hotels = [0, 195, 212, 370, 450, 530, 670, 700, 800, 920, 970, 1085, 1130, 1220, 1350, 1440, 1600]

    def penalty(self, n1:int, n2:int) -> int:

        distance = self.hotels[n2]- self.hotels[n1]
        penalty = pow((200-distance),2)

        return penalty

    def plan_trip(self):
        INFINITY = 999999
        best = [INFINITY]*(len(self.hotels))
        best[0] = 0
        prev = [-1] * (len(self.hotels))


        for i in range (1, len(self.hotels)):
            for j in range(0,i):
                dist = self.hotels[i] - self.hotels[j]
                penalty = self.penalty(j,i)
                if best[j] + penalty < best[i]:
                    best[i] = best[j] + penalty
                    prev[i] = j

        stops = []
        t = len(self.hotels)-1

        while t > 0:
            stops.append(t)
            t = prev[t]

        stops.reverse()

        return best[len(self.hotels)-1], stops



if __name__ == "__main__":
    rt = RoadTripClass()
    print(rt.plan_trip())





