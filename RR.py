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

def RR(dataset, quantum):
    quantum = quantum    
    avg_WT = 0
    WT = [0 for _ in range(len(dataset))]            
    BT = [i for i in dataset['BurstTime']]
    time=0
    i=0                                           
    while(1):                                                  
        if(BT[i]== -100):                                    
            pass                                              
        elif(BT[i]>quantum):                                
            print("|", " "*quantum, dataset.index[i], end=" ")  
            BT[i] -= quantum                                      
        else:                                                   
            print("|", " "*BT[i], dataset.index[i], end=" ")  
            BT[i] = -100                                       
        i+=1  
        i = i%(len(dataset))  
        if(all([(BT[i]==-100) for i in range(len(BT))])):   
            break
        
    print("|")
    print(0, end=" ")    
    BT = [i for i in dataset['BurstTime']]     
    i=0      
    while(1):
        if(BT[i]== -100):
            pass
        elif(BT[i]>quantum):                            
            time += quantum
            WT[i] -= quantum                              
            print(" "*(quantum+2), time, end=" ")        
            BT[i] -= quantum                             
        else:
            time += BT[i]                                
            WT[i] += time - BT[i]                      
            print(" "*(BT[i]+2), time, end=" ")
            BT[i] = -100                                
        i+=1
        i = i%(len(dataset))
        if(all([(BT[i]==-100) for i in range(len(BT))])):
            break
            
    print("\n")
    for i in range(len(WT)):                                   
        print("Waiting Time P{0}: {1}".format(i+1,WT[i]))
        avg_WT += WT[i]
        
    print("\n")
    print("Average Waiting Time: {}".format(avg_WT/len(BT)))
    

if __name__ == '__main__':
    RR(dataset1, 12)   
    RR(dataset2, 5)   