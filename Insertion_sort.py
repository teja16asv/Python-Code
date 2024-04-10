arr=[]
n=int(input("enter how many you want? "))
print("enter %d elements"%n)
for i in range(0,n):
    element=int(input())
    arr.append(element)
for i in range(1, len(arr)):
    print(arr[i])