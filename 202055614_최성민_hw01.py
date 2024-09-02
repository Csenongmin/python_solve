#컴퓨터알고리즘[061] 정보컴퓨터공학부 202055614 최성민
import sys
input = sys.stdin.readline

def partition(E, pivot, first, last):
    leftmark = first+1
    rightmark = last

    while rightmark >= leftmark:
        if E[leftmark] < pivot:
            leftmark+=1
            continue
            
        elif E[rightmark] > pivot:
            rightmark-=1
            continue
        
        temp = E[rightmark]  #switch
        E[rightmark] = E[leftmark]
        E[leftmark] = temp
        
    return rightmark  #split point



def quick_sort(arr, first, last):
    if(first < last):
        pivot = arr[first]
        splitPoint = partition(arr,pivot,first,last)
        # switch pivot and split point
        temp = arr[splitPoint]  
        arr[splitPoint] = pivot
        arr[first] = temp
        #recursive calls
        quick_sort(arr, first, splitPoint - 1)
        quick_sort(arr, splitPoint+1, last)
    return

N = int(input().strip())

arr = list(map(int, input().split()))

quick_sort(arr, 0, N-1)

for elem in arr:
    print(elem, end=" ")
