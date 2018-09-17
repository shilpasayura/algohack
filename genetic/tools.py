#tools.py
'''
AlgoHack Genetic Algorithm for University Semaster Planning
Version 0.03 2018
Niranjan Meegammana Shilpasayura.org
'''
def sort_dict_val(L):
    sorted_by_value = sorted(L.items(), key=lambda kv: kv[1])
    L=dict(sorted_by_value)
    return L

def sort_dict_key(L):
    L1={}
    for key in sorted(L):
        #print(key, L[key])
        L1[key]=L[key]
    return L1

def sort_dict_val_len(L):
    L1={}
    for key in L:
        n=len(L[key])
        L1[key]=n

    L2= sorted(L1.items(), key=lambda kv: kv[1])    
    L3=dict(L2)
    L4={}
    for key in L3:
        L4[key]=L[key]
    #print (L4)
    return L4

if __name__ == "__main__":
    L = {"7": 7, "3": 4, "4": 3, "2": 1, "1": 0}
    L1=sort_dict_val(L)
    print(L1)
    L2=sort_dict_key(L)
    print(L2)
    
