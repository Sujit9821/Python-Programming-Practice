import random
def insert_d(u_list,item):
    if len(u_list)==0 or u_list[-1]<=item:
        u_list.append(item)
        return
    item2 = u_list[-1]
    u_list.pop()
    insert_d(u_list,item)
    u_list.append(item2)
def sort_d(u_list):
    if len(u_list) <=1:
        return
    item = u_list[-1]
    u_list.pop()
    sort_d(u_list)
    insert_d(u_list,item)
if __name__ == "__main__":
    range_min = int(input("Give a minimum value of a range: "))
    range_max = int(input("Give a maximum value of a range: "))
    number_of_elements = int(input("Give number of elements you want to randomnly sort: "))
    u_list = [random.randint(range_min,range_max) for _ in range(number_of_elements)]
    print("Unsorted list: ",u_list)
    sort_d(u_list)
    print("Sorted list is: ",u_list)