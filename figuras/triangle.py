import sys
import random
import time

def draw(x,num,space):
    token =x
    if token <=num:
        print (" "*space*2 +" "*((num-token)//2)+"*"*token)
    #if token > num:
    #    a = num*2-token
    #    print (" "*space*2 +" "*((num-(num*2-token))//2)+ "*"*(num*2-token))

#num = int(input("Ingrese un numero"))
def main():
#    while True:
        num = random.randint(6,19)
        space = random.randint(1,46)
        #num = 9
        if num %2 == 0:
            num = num+1
        _var = num*2


        for x in range(_var):
            if x%2 != 0:
                draw(x,num,space)

        time.sleep(1)
#except KeyboardInterrupt:
#    print ("")
if __name__ == "__main__":
    main()
