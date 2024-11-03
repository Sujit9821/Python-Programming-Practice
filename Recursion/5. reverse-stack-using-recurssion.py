import random
def insert(u_list,item):
    if len(u_list)==0:
        u_list.append(item)
        return
    item2 = u_list.pop()
    insert(u_list,item)
    u_list.append(item2)
def rev_list(u_list,k):
    
    if k==0:
        return
    item = u_list.pop()
    
    rev_list(u_list,k-1)
    insert(u_list,item)
if __name__ == "__main__":
    range_min = int(input("Give a minimum value of a range: "))
    range_max = int(input("Give a maximum value of a range: "))
    number_of_elements = int(input("Give number of elements you want to randomnly sort: "))
    u_list = [random.randint(range_min,range_max) for _ in range(number_of_elements)]
    k = len(u_list)
    print("u_list: ",u_list)
    rev_list(u_list,k)
    print("rev_list: ",u_list)