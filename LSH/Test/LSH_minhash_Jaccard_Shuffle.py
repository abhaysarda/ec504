"""
Using the LSH_minhash_Jaccard_Shruthi.py to find percentage similarity between two documents:

Variables a,b,c are used to store the contents of the documents. The contents can be changed/updated. Run

``python3 LSH_minhash_Jaccard_Shruthi.py``

The output will be a percentage measure of the similarity between each pair of documents.

For the sample sentences:

a = "Who was the first king of Poland"
b = "Who was the first ruler of Poland"
c = "Who was the last pharaoh of Egypt",

the output would look as follows-

>0.7450980392156863 0.29411764705882354 0.3333333333333333

This indicates the higher measure of similarity between sentences a and b as compared to (a,c) and (b,c).

"""
import random
a = list("Who was the first king of Poland".split())
b = list("Who was the first ruler of Poland".split())
c = list("Who was the last pharaoh of Egypt".split())
minHash_a = []
minHash_b = []
minHash_c = []
iteration = 50
def preProcess(a,b,c):
    num = 0
    word = {}
    col_a = {}
    col_b ={}
    col_c ={}
    setA = set(a)
    setB = set(b)
    setC = set(c)
    #index array for minhashing
    x = list(setA.union(setB).union(setC))
    random.shuffle(x)
    # word array and sentence arrays
    for val in x:
        num+=1
        word[num] = val

        if val in a:
            col_a[num] = 1
        else:
            col_a[num] = 0

        if val in b:
            col_b[num] = 1
        else:
            col_b[num] = 0

        if val in c:
            col_c[num] = 1
        else:
            col_c[num] = 0

    #print(word)
    MinHash(col_a,col_b,col_c)


def MinHash(col_a,col_b,col_c):
    global iteration
    while iteration >=0:
        s = 1
        for k,v in col_a.items():
            if v == 1 and s == 1:
                minHash_a.append(k)
                s = 0
        s = 1
        for k,v in col_b.items():
            if v == 1 and s == 1:
                minHash_b.append(k)
                s = 0
        s = 1
        for k,v in col_c.items():
            if v == 1 and s == 1:
                minHash_c.append(k)
                s = 0
        iteration = iteration - 1

        preProcess(a,b,c)



def Jaccard(a,b):
    same = 0.0
    for i in range(0, len(a)):
        if a[i] == b[i]:
            same=same+1
    return same/len(a)


preProcess(a,b,c)

print(minHash_a)
print(minHash_b)
print(minHash_c)
print(Jaccard(minHash_a,minHash_b),Jaccard(minHash_a,minHash_c), Jaccard(minHash_b, minHash_c))
