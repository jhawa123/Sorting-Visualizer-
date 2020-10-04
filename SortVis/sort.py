count=[0]
def swap(A, i, j):
    if i != j:
        A[i], A[j] = A[j], A[i]
def insertionsort(A,bar_rects):
    for i in range(1, len(A)):
        j = i
        bar_rects[0].set_color('g')
        while j > 0 and A[j] < A[j - 1]:
            swap(A, j, j - 1)
            bar_rects[j].set_color('g')
            bar_rects[j-1].set_color('g')
            j -= 1
            count[0]+=1
            yield A
        
def bubblesort(A,bar_rects):
    for i in range(len(A)):
        if i==len(A)-2:
            bar_rects[0].set_color('g')            
        bar_rects[len(A)-i-1].set_color('g')
        for j in range(len(A)-1-i):
            if A[j]>A[j+1]:
                swap(A,j,j+1)
                count[0]+=1
            yield A

def selectionsort(A,bar_rects):
    for i in range(len(A)):
        min=A[i]
        mpos=i
        for j in range(i+1,len(A)):
            if A[j]<min:
                min=A[j]
                mpos=j
            yield A
        swap(A,i,mpos)
        count[0]+=1
        bar_rects[i].set_color('g')
        yield A

def quicksort(A, start, end,bar_rects):
    if start>=end:
        return
    pivot = A[end]
    pivotIdx = start

    for i in range(start, end):
        if A[i] < pivot:
            swap(A, i, pivotIdx)
            count[0]+=1
            bar_rects[i].set_color('g')
            bar_rects[pivotIdx].set_color('g')
            pivotIdx += 1
        yield A
    swap(A, end, pivotIdx)
    count[0]+=1
    bar_rects[end].set_color('g')
    bar_rects[pivotIdx].set_color('g')    
    yield A
    yield from quicksort(A, start, pivotIdx - 1,bar_rects)
    yield from quicksort(A, pivotIdx + 1, end,bar_rects)

def mergesort(A, start, end,bar_rects):
    if end <= start:
        return
    mid = start + ((end - start + 1) // 2) - 1
    yield from mergesort(A, start, mid,bar_rects)
    yield from mergesort(A, mid + 1, end,bar_rects)
    yield from merge(A, start, mid, end,bar_rects)
    yield A
def merge(A, start, mid, end,bar_rects):  
    merged = []
    leftIdx = start
    rightIdx = mid + 1

    while leftIdx <= mid and rightIdx <= end:
        if A[leftIdx] < A[rightIdx]:
            count[0]+=1
            merged.append(A[leftIdx])
            bar_rects[leftIdx].set_color('g')
            leftIdx += 1
        else:
            count[0]+=1
            merged.append(A[rightIdx])
            bar_rects[rightIdx].set_color('g')
            rightIdx += 1
    while leftIdx <= mid:
        count[0]+=1
        merged.append(A[leftIdx])
        bar_rects[leftIdx].set_color('g')
        leftIdx += 1
    while rightIdx <= end:
        count[0]+=1
        merged.append(A[rightIdx])
        bar_rects[rightIdx].set_color('g')
        rightIdx += 1
    for i, sorted_val in enumerate(merged):
        A[start + i] = sorted_val
        yield A

def heapify(A,n, i,bar_rects): 
	largest = i 
	l = 2 * i + 1
	r = 2 * i + 2
	if l < n and A[i] < A[l]: 
		largest = l 
	if r < n and A[largest] < A[r]: 
		largest = r 
	if largest != i: 
		A[i],A[largest] = A[largest],A[i]
		count[0]+=1
		bar_rects[i].set_color('g')
		bar_rects[largest].set_color('g')
		yield from heapify(A,n,largest,bar_rects)
		yield A
		 
def heapsort(A,bar_rects): 
	n = len(A) 
	for i in range(n//2 - 1, -1, -1): 
		yield from heapify(A, n, i,bar_rects) 
	for i in range(n-1, 0, -1): 
		A[i], A[0] = A[0], A[i]
		count[0]+=1
		bar_rects[i].set_color('g')
		bar_rects[0].set_color('g')
		
		yield from heapify(A, i, 0,bar_rects)
		yield A
		


