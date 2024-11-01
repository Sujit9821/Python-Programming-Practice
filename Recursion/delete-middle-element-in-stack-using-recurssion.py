import random
def remove_middle(stack,k):
    if k==1:
        stack.pop()
        return
    item = stack.pop()
    remove_middle(stack,k-1)
    stack.append(item)
if __name__ == "__main__":
    range_min = int(input("Give a minimum value of a range: "))
    range_max = int(input("Give a maximum value of a range: "))
    number_of_elements = int(input("Give number of elements you want to make a random stack: "))
    stack = [random.randint(range_min,range_max) for _ in range(number_of_elements)]
    print("Original Stack: ",stack)
    middle_position = len(stack)//2 +1
    remove_middle(stack,middle_position)
    print("After removing middle element from the stack: ",stack)