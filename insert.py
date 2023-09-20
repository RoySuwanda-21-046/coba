
def insertionSort (listdata) :
    for outIter in range (1, len(listdata)) :
        print(listdata)
        key = listdata[outIter]
        ind= outIter
        while(ind >0 and listdata[ind-1]>key) :
            listdata[ind]=listdata[ind-1]
            ind=ind-1
            print ("inner =", listdata)
        listdata[ind] = key
    print("sorteddata=",listdata)
a = [10,2,5,8,1,20,2,2,4]
insertionSort (a)