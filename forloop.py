class looper:

    def breaker(self):
        print("breaker 1\n")
        global loop
        loop= ['a','b','j','k','l']

        for i in loop:
            print(i)
            if i== 'j':
                break
        
        print("breaker 2 \n")
        for i in loop:
            if i== 'j':
                break
            print(i)


    def continuing(self):
        print("continuing 1\n")
        for i in loop:
            print(i)
            if i== 'j':
                continue
        
        print("continuing 2\n")
        for i in loop:
            if i== 'j':
                continue
            print(i)

obj = looper()
obj.breaker()
obj.continuing()

