from itertools import count
import re
import string

class Filereader:

    def getchart(self):
        file = open("Apache_2k.log")

        counter = 0
        print("Date \t \t \t \t clent ip \n")
        while file.readline() != "":
            i = (file.readline())
            if re.findall('error',i) :
                # client_ip = i.split("[c")[0]
                # client_ip = i.split(str(re.findall("^\[Client", i)))[1]

                try:
                    client_ip1 = i.split("[client")[1]

                    client_ip = client_ip1.split("]")[0]
                    
                except IndexError:
                    date = i.split("] ")[0]
                    continue
                
                
                print((date), "\t \t ", ( client_ip ))
                counter += 1

        print("Total number of forbden requests are",counter)


obj = Filereader()
obj.getchart()



