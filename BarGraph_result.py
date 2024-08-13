import pandas as pd
import matplotlib.pyplot as plt 

data1 = {'Process': ['P1','P2','P3','P4','P5'],
        'BurstTime': [10,29,3,7,12],
        'Priority': [5,1,3,4,2]
        }
dataset1 = pd.DataFrame(data1)
dataset1.set_index('Process', inplace=True)

data2 = {'Process': ['P1','P2','P3','P4','P5'],
         'BurstTime': [2,1,8,4,5],
         'Priority': [2,1,4,2,3]
        }
dataset2 = pd.DataFrame(data2)
dataset2.set_index('Process', inplace=True)

    
def avg_WT_FCFS(dataset):
    avg_WT=0       
    WT = [0 for _ in range(len(dataset))]  
    BT = [i for i in dataset['BurstTime']] 
        
    time=0                          
    for i in range(len(dataset)):   
        time += BT[i]              
        WT[i] = time - BT[i]
        avg_WT += WT[i] 
        
    return avg_WT/len(WT)

def avg_WT_RR(dataset, quantum):
    quantum = quantum
    BT = [i for i in dataset['BurstTime']]
    WT = [0 for _ in range(len(dataset))]
    i=0
    time=0
    while(1):
        if(BT[i]== -100):
            pass
        elif((BT[i]-quantum)<=0):
            time += BT[i]
            WT[i] += time - BT[i]
            BT[i] = -100
        else:
            time += quantum
            WT[i] -= quantum
            BT[i] -= quantum
        i+=1
        i = i%(len(dataset))
        if(all([(BT[i]==-100) for i in range(len(BT))])):
            break
            
    avg_WT = 0
    for i in range(len(WT)):
        avg_WT += WT[i]
        
    return avg_WT/len(BT)
    
def avg_WT_Priority(dataset):
    avg_WT=0       
    WT = [0 for _ in range(len(dataset))]
    sorted_set = dataset.sort_values(by=['Priority','BurstTime'])       
    BT = [i for i in sorted_set['BurstTime']]                  
    time=0                                          
    for i in range(len(sorted_set)):    
        time += BT[i]             
        WT[i] = time - BT[i]
        avg_WT += WT[i] 
        
    return avg_WT/len(WT)
        
def avg_WT_SJF(dataset):
    avg_WT=0       
    WT = [0 for _ in range(len(dataset))]
    sorted_set = dataset.sort_values(by=['BurstTime','Priority'])       
    BT = [i for i in sorted_set['BurstTime']]                  
    time=0                                          
    for i in range(len(sorted_set)):    
        time += BT[i]             
        WT[i] = time - BT[i]
        avg_WT += WT[i] 
        
    return avg_WT/len(WT)

def BarPlot(dataset,quantum):
    
    avg_WT = [avg_WT_FCFS(dataset), avg_WT_RR(dataset,quantum), avg_WT_Priority(dataset), avg_WT_SJF(dataset)]
    Schedule_Name = ['FCFS', 'RR', 'Priority', 'SJF']
    plt.bar(Schedule_Name,avg_WT)
    plt.xlabel("Scheduling Algorithm")
    plt.ylabel("Average Waiting Time")
    plt.show()
if __name__ == '__main__':
    
    BarPlot(dataset1, 12)
    BarPlot(dataset2, 5)
