import math
import random

def countNeighbours(x): #m(x)
    count = 0
    for i in range(0,len(x)-1):
        if x[i] == x[i+1]:
            count+=1
    return count

def random_x(d):
    x=[]
    for i in range(0,d):
        x.append(int(round(random.randint(0,1))))
    return x

def flip_rand_bit(x):
    x = x[:]
    bit = random.randint(0,len(x)-1)
    x[bit]= 1 - x[bit]
    return x

def avg_neighbours(a_list):
    total=0
    for i in range(0,len(a_list)):
        total+= countNeighbours(a_list[i])
    return total/len(a_list)
        
def main():
    d = int(input("dimension: "))
    beta = float(input("beta: "))
    
    x0 = random_x(d) #generate initial state
    data_list = [x0] #will store all the samples we generate
    i=0

    while i < 1000000:
        x_prime = flip_rand_bit(data_list[i])

        neighbour_diff = countNeighbours(x_prime)-countNeighbours(data_list[i]) #difference between candidate's neighbours and old neighbours
        
        rate = min(1,math.exp(beta*neighbour_diff)) #T's cancel out
        
        x_next = data_list[i] #next one will be old one by default

        u = random.uniform(0,1) #generate random uniform num

        if u < rate or u==rate:
            x_next = x_prime

        data_list.append(x_next)
        i+=1
        
    print(avg_neighbours(data_list))     

if __name__ == '__main__':
    main()


        
