
class IncreasingSequencesClass:

    list_a = [5, 1, 4, 2, 3, 6]
    list_b = [36, 13, 78, 85, 16, 52, 58, 61, 63, 83, 46, 19, 85, 1, 58, 71, 26, 26, 21, 31]
    list_c = [2, 22, 32, 35, 66, 59, 79, 64, 48, 96, 7, 39, 18, 15, 45, 89, 3, 81,
              26, 26, 31, 55, 10, 91, 70, 61, 12, 87, 13, 31, 27, 58, 71, 75, 32,
              63, 98, 77, 92, 43, 66, 32, 11, 65, 1, 80, 14, 99, 29, 91]

    def __init__(self,v):

        self.L = [1 for i in range (len(v))]
        self.L_list = [[v[l]] for l in range (len(v))]

        for i in range (len(v)):

            for j in range (i-1, -1, -1):
                if v[j] < v[i]:

                     if self.L[j]+1 > self.L[i]:
                        self.L[i] = self.L[j]+1
                        self.L_list[i] = self.L_list[j] + [v[i]]


        self.list_longest =  self.L_list[self.L.index(max(self.L))]


    def find_max_len(self):
        return max(self.L)

    def find_max_list(self):
        return self.list_longest


new = IncreasingSequencesClass(IncreasingSequencesClass.list_c)
print(new.find_max_len())
print(new.find_max_list())















