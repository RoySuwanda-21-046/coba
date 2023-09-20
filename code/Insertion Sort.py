a = [10, 5, 7, 9]

for i in range(1, len(a)):
    key = a[i]
    print(key)
a = [10, 5, 7, 9]

for i in range(1, len(a)):
    key = a[i]
    print(key)
    j = i-1
    while j >= 0:
        print('j', j)
        j -= 1
a = [10, 5, 7, 9]

for i in range(1, len(a)):
    key = a[i]
    print(key)
    j = i-1
    while j >= 0 and key <= a[j]:
        # print('j',j)
        a[j+1] = a[j]
        j -= 1
        print(j, '=', a)
    a[j+1] = key  # insert key nya
    print(a)

# Ascending tetapi proses pengurutan dimulai dari indeks-indeks terakhir, bukan pertama


def ascending(data):
    n = len(data)
    for i in range(n-2, -1, -1):
        print('Data : ', data)
        key = data[i]
        print('key, data [{}] : {}'.format(i, data[i]))
        count = i
        while (count < n-1) and (key < data[count+1]):
            data[count] = data[count+1]
            print('Inner Sorting = ', data)
            count += 1
        data[count] = key
    print('sortedData = ', data)


b = [3, 1, 12, 5, 1, 2, 0, 8, 4]
ascending(b)

# Descending tetapi proses pengurutan dimulai dari indeks-indeks awal Silahkan bermain-main indeks spy bs memahami jalannya pengurutan


def Descending(listData):

    for outIter in range(1, len(listData)):
        print(listData)
        key = listData[outIter]
        ind = outIter
        while (ind > 0 and listData[ind-1] > key):
            listData[ind] = listData[ind-1]
            ind = ind-1
            print('inner=', listData)
        listData[ind] = key
    print('sortedData=', listData)
