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

def SJF(dataset):
    avg_WT=0      
    WT = [0 for _ in range(len(dataset))]
    sorted_set = dataset.sort_values(by=['BurstTime','Priority'])        
    BT = [i for i in sorted_set['BurstTime']]                   
    
    for i in range(len(sorted_set)):          
        print("|", " "*BT[i], sorted_set.index[i], end=' ')
        
    print("|")
    print(0, end=" ")
    time=0         
                                    
    for i in range(len(sorted_set)):    
        time += BT[i]             
        WT[i] = time - BT[i]
        print(" "*(BT[i]+2), time, end=" ") 
        
    print("\n")
    for i in range(len(sorted_set)):                        
        print("Waiting Time {0}: {1}".format(sorted_set.index[i], WT[i]))
        avg_WT += WT[i] 
        
    print("\n")
    print("Average Waiting Time: {}".format(avg_WT/len(WT))) 
    
if __name__ == '__main__':
    SJF(dataset1)
    SJF(dataset2)