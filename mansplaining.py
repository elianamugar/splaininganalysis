"""
Author: Eliana Mugar
"""

#requires download of nltk in python
import os
import nltk

def main():
    male_giver_check = False
    female_follower_check = False
    giver_start = False
    save_index = 0
    male_female_count = 0
    # establish text_file variable as git1
    # modify path for where files are on machine
    path = '''D:\EVL\Script Projects\Map Corpus\Map_Task_Processed\Fit_Files\git1'''
    for text_file in os.listdir(path):
        if '.txt' in text_file:
            my_file = os.path.join(path, text_file)
            f = open(my_file, 'r+')
            raw = f.read()
            tokens = nltk.word_tokenize(raw)
            for i in range(len(tokens)):
                # find Giver
                if tokens[i] == "male":
                    male_giver_check = True
                    for j in range(i, len(tokens)):
                        if tokens[j] == "female":
                            female_follower_check = True
                if tokens[i] == "who=G" and tokens[i + 1] == "n=1":
                        giver_start = True
            if male_giver_check and female_follower_check:
                print(text_file[:5])
                currentpath = '''D:\EVL\Script Projects\Map Corpus\Map_Task_Processed\Fit_Files\git2'''
                my_file = os.path.join(currentpath, text_file[:5] + "_fit2.txt")
                f = open(my_file, 'r+')
                raw = f.read()
                tokens = nltk.word_tokenize(raw)
                if giver_start:
                    for line in tokens:
                        line = line.strip("\n")
                        words = line.split()
                    print("lines: ", line, "words: ", words)
                else:
                    print("not giver start test")
                male_giver_check = False
                female_follower_check = False
                giver_start = False

                # check corresponding fit2 file, and just count follower lines
                # count the male giver word count
                    # don't count info in the curly brackets
                    # or strip files of curly brackets? er...
                    # clear punctuation
                # get average of male giver word count?


while True:
    answer = input("Run the 'Mansplaining Analysis' program? (y/n): ")
    if answer not in ('y', 'n'):
        print("Invalid input.")
        break
    if answer == 'y':
        main()
    else:
        print("Goodbye.")
        break