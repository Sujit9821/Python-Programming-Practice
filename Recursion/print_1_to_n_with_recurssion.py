def print_r(n):
    if n==1:
        print(n)
        return 1
    print_r(n-1)
    print(n)
if __name__ == "__main__":
    n = int(input("Give upto which you want to print: "))
    if n<=0:
        print("User should provide value more than 0.")
    else:
        print_r(n)