# Sort an Array of 0's and 1's

# Input ---> [0,1,1,1,0,0,1,2,2,2,0,1]
#Output ---> [0,0,0,0,1,1,1,1,1,2,2,2]

#Method to print array

def arr(arr,n):
    for i in range(n):
        print(arr[i],end="")

#Method to sort array of 0,1 and 2
def sort_arr(arr,n):
    count_0 = 0
    count_1 = 0
    count_2 = 0

    for i in range(n):
        if arr[i] == 0:
            count_0 += 1
        elif arr[i] == 1:
            count_1 += 1
        elif arr[i] == 2:
            count_2 += 1

    i = 0
    while count_0 >0:
        arr[i] = 0
        i+=1
        count_0 -=1

    while count_1 > 0:
        arr[i] = 1
        i+=1
        count_1 -= 1

    while count_2 > 0:
        arr[i] = 2
        i+=1
        count_2 -= 1
    print(arr)

#Main Method

if __name__ == "__main__":
    print("Enter the List of array of 0's, 1's and 2's")
    arr = list(map(int,input().split()))
    n = len(arr)
    arr = arr[:n]
    sort_arr(arr,n)
