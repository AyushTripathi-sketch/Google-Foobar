#list containing no. who are sum of n natural numbers
l=[1,3,6,10,15,21,28,36,45,55,66,78,91,105,120,136,153,171,190,210] 

def search(list,number_to_check):

    for i in range(0,len(list)):
        if(l[i]>number_to_check):
            return i

def solution(n):

    length = search(l,n)
    c=0
    l1=[]

    for i in range(1,length+1):
        l1.append(i)

    l1.sort(reverse=True)

    if(sum(l1)!=n):
        l1[0]=n-sum(l1)+l1[0]

    if(True):
        c += 1
        l2 = []
        l2 = l2 +l1
        k=2
        

        while(len(l2)>2):

            if (l1[0]-l1[1]>2):
                while (l1[0]-l1[1]>2):
                    print(l1)
                    l1[0] -= 1
                    l1[1] += 1
                    c +=1
            

            while len(l1)>k:
                print(l1)
                l1[1] = l1[0] + l1[1]
                l1.remove(l1[0])
                c += 1
            
                while (l1[0]-l1[1]>2):
                    print(l1)
                    l1[0] -= 1
                    l1[1] += 1
                    c  += 1

            print(l1)
            
            
            l2[0]=l2[len(l2)-1]+l2[0]
            l2.remove(l2[len(l2)-1])
            l1=[]
            l1 = l1 +l2
            k=3
            c += 1
            
            
            return c
