import pandas as pd

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

def FCFS(dataset):
    avg_WT=0       
    WT = [0 for _ in range(len(dataset))]  
    BT = [i for i in dataset['BurstTime']]
    time=0 
    
    for i in range(len(dataset)):          
        print("|", " "*BT[i], dataset.index[i], end=' ')
        
    print("|")
    print(0, end=" ")    
    
    for i in range(len(dataset)):   
        time += BT[i]              
        WT[i] = time - BT[i]
        print(" "*(BT[i]+2), time, end=" ")  
        
    print("\n")
    for i in range(len(dataset)):                         
        print("Waiting Time P{0}: {1}".format(i+1, WT[i]))
        avg_WT += WT[i] 
        
    print("\n")
    print("Average Waiting Time: {}".format(avg_WT/len(WT))) 
        

if __name__ == '__main__':
    FCFS(dataset1)
    FCFS(dataset2)