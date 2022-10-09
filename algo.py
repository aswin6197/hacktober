## Code to merge two sorted lists

def merge(A, B):
        i=0
        j=0
        while i<len(A) and j<len(B):
            if A[i]<B[j]:
                i+=1
            else:
                A.insert(i,B[j])
                j+=1
        if j<len(B):
            while j<len(B):
                A.append(B[j])
                j+=1