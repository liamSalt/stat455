import random
import math

def next_state(state):
    transition = [[0,1],[0,2],[0,3]]

    if state == 3:
        return state

    coin = random.randint(0,1)
    new_state = transition[state][coin] 
    return new_state

def experiment():
    state = 0
    time = 0

    while state < 3:
        state = next_state(state)
        time +=1
    return time

def stdev(data,mean):
    sum_=0
    for j in range(0,len(data)):
        sum_+= (data[j]-mean)**2
    sum_ = math.sqrt(sum_/(len(data)-1))
    return sum_
    
def main():
    mean_time = 0
    trials = 100000
    times=[]
    for i in range(0,trials):
        newVal= experiment()
        times.append(newVal)
        mean_time += newVal
        
    mean_time = mean_time/trials
    sd = stdev(times,mean_time)
    
    print("Mean time after "+ str(trials) + " trials: " + str(mean_time))
    print("Standard Deviation after "+ str(trials) + " trials: " + str(sd))
    

if __name__ =="__main__":
    main()
