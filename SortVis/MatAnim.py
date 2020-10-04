import random
from flask import Flask ,render_template,request,send_file,Response
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from sort import *
from io import BytesIO 
app=Flask("_SortVis_")

@app.route('/')
def index():
    return render_template('Sorting.html')

@app.route('/sortvis',methods=['POST'])
def sort_vis():
    n=int(request.form['array length'])
    A= random.sample(range(1, 200),n)
    fig, ax = plt.subplots()
    bar_rects = ax.bar(range(int(len(A))), A, align="edge",color='blue')
    text1 = ax.text(0.02, 0.95, "", transform=ax.transAxes)
    text2=  ax.text(0.02, 0.90, "", transform=ax.transAxes)
    text3=  ax.text(0.02, 0.85, "", transform=ax.transAxes)

    choice=request.form['sort']
    opt=0
    if choice=='insertion':
        opt=1
        title = "Insertion sort"
        generator = insertionsort(A,bar_rects)
    elif choice=='bubble':
        opt=2
        title = "BuBBle sort"
        generator = bubblesort(A,bar_rects)
    elif choice=='selection':
        opt=3
        title = "Selection sort"
        generator = selectionsort(A,bar_rects)
    elif choice=='quick':
        opt=4
        title = "Quick sort"
        generator = quicksort(A,0,len(A)-1,bar_rects)
    elif choice=='merge':
        opt=5
        title = "Merge sort"
        generator = mergesort(A,0,len(A)-1,bar_rects)
    elif choice=='heap':
        opt=6
        title = "Heap sort"
        generator = heapsort(A,bar_rects)
        
    ax.set_title(title)
    ax.set_xlabel("Index")
    ax.set_ylabel("Value")

    stime=time.time()
    iteration = [0]

    def update_fig(A, rects, iteration):
        for rect, val in zip(rects, A):
            rect.set_height(val)    
        iteration[0] += 1
        etime=time.time()-stime
        if opt<4:
            text1.set_text("Number of Slidings and Swaps: {}".format(iteration[0]))
        else:
            text1.set_text("Number of Slidings: {}".format(iteration[0]))
        text2.set_text("Time elapsed: %.3f sec"% etime)
        if opt>=4:
            text3.set_text("Number of Operations:{}".format(count[0]))
    anim = animation.FuncAnimation(fig, func=update_fig,fargs=(bar_rects, iteration), frames=generator, interval=20,repeat=False,blit=False)
    plt.show()
    count[0]=0
    return render_template('Sorting.html')
app.run(host='localhost',port=2000)


              
