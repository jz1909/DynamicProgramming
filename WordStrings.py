from ast import parse
from tkinter import filedialog
from tkinter import Tk

class WordStringsClass:



    def __init__(self):

        self.word_list = []

    def load_words(self):
        root = Tk()
        print(
            "Showing file dialog. Make sure it isn't hiding! \nClick on the small window in the upper left corner of\nthe screen. It may be behind the pycharm window.")
        word_filename = filedialog.askopenfilename()
        root.update()
        if word_filename == "":
            raise IOError("No file found...")
        self.load_words_from_file(word_filename)

    def load_words_from_file(self, word_filename: str):
        print(f"Loading words from {word_filename}.")
        self.word_list = []
        with open(word_filename, 'r', encoding='utf-8') as ins:
            for count, line in enumerate(ins):
                word = line.strip()
                if not word:
                    continue
                self.word_list.append(word)
                if count % 100 == 0:
                    print(f"  {count} words loaded…")
        print("Done loading words.\n" + "-" * 40)





    def word_strings(self, parseword):

        parseword = parseword.lower()

        L = [False]*(len(parseword)+1)
        L[0] = True

        for i in range (1, len(parseword)+1):
            for j in range (0, i):
                if L[j] == True and parseword[j:i] in self.word_list:
                    L[i] = True
                    break


        return L[len(parseword)]

if __name__ == "__main__":
    words = WordStringsClass()

    words.load_words_from_file("word_list_moby_crossword_flat2024.txt")
    # print(words.word_strings("Ihateyou"))
    print(words.word_strings("theunanimousdeclarationofthethirteenunitedstatesofamericawheninthecourseofhumaneventsitbecomesnecessaryforonepeopletodissolvethepoliticalbandswhichhaveconnectedthemwithanotherandtoassumeamongthepowersoftheearththeseparateandequalstationtowhichthelawsofnatureandofnaturesgodentitlethemadecentrespecttotheopinionsofmankindrequiresthattheyshoulddeclarethecauseswhichimpelthemtotheseparationweholdthesetruthstobeselfevidentthatallmenarecreatedequalthattheyareendowedbytheircreatorwithcertainunalienablerightsthatamongthesearelifelibertyandthepursuitofhappinessthattosecuretheserightsgovernmentsareinstitutedamongmenderivingtheirjustpowersfromtheconsentofthegovernedthatwheneveranyformofgovernmentbecomesdestructiveoftheseendsitistherightofthepeopletoalterortoabolishitandtoinstitutenewgovernmentlayingitsfoundationonsuchprinciplesandorganizingitspowersinsuchformastothemshallseemmostlikelytoeffecttheirsafetyandhappiness"))