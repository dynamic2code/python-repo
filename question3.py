import requests
from bs4 import BeautifulSoup

class Bookreader:

    def getfiles(self):
        
        global chapters, no_word_list


        responde = requests.get("https://www.gutenberg.org/files/11/old/alice30.txt")
        soup = BeautifulSoup(responde.content, 'html.parser')

        text = responde.text
        chapters = text.split("CHAPTER")

        # getting the word count

        file = requests.get("https://cse2050.drfitz.fit/data/very/stop_words.txt")

        no_word_list =(file.text.split("\""))



    def showdata(self, chapters, no_word_list):
        print("CHAPTER \t \t \t CHAPTER TITLE \t \t \t UNIQUE WORD COUNT")
        for i  in chapters:
                if i == chapters[0]:
                    continue
            # print(i,"ewertrytfuygiuipjok[zdxcfyvbnk;ml,'zsnkjmdxfvyhbujcgvyhbujnkm")
            # print(chapters[i])
            
                il = i.split(" ")
                li = (i.split("\n"))
                title = li[2]
                chapter = li[0]
                words= []                  

                for word in li:

                    if word not in no_word_list:
                        words.append(word)
                print( "  chapter  ",chapter," \t \t \t ", (title.strip()) ,"\t \t \t", len(words))


obj = Bookreader()
obj.getfiles()
obj.showdata(chapters, no_word_list)



