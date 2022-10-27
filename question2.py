import csv

class Bonus:

    def getdata(self):
        file = "Untitled spreadsheet - IMDb_movies.csv"
        global length, countries, data

        countries =[]
        length = []
        with open(file, encoding="utf8") as csvfile:
            reader = csv.reader(csvfile)

            all = []
            for row in reader:
                all.append(row[7])
        # print(all)
        countries_b4 = []
        length_b4 = []
        for i in all:
            data =[i,all.count(i)]
            
            countries_b4.append(data[0])
            length_b4.append(data[1])

            print('running...')

        # print(countries_b4)
        # print(length_b4)

        countries = countries_b4[1:9]
        length = length_b4[1:9]

        # unpacking countries to match their lengths into sets which will be then stored in data
        # data  = zip(countries, length)
        data = []

        for x in zip(countries,length):
            data.append(x)


        

        # print(data) 

    def preparedata(self, data):
        
       
        max_value = max(count for _, count in data)
        increment = max_value / 25

        longest_label_length = max(len(label) for label, _ in data)
        for label, count in data:

            bar_chunks, remainder = divmod(int(count * 8 / increment), 8)
            bar = '█' * bar_chunks
            if remainder > 0:
                bar += chr(ord('█') + (8 - remainder))
            bar = bar or  '▏'

            print(f'{label.rjust(longest_label_length)} ▏ {count:#4d} {bar}')

obj = Bonus()
obj.getdata()
obj.preparedata(data)
