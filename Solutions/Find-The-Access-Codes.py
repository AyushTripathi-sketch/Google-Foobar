def solution(l):

    m=len(l)-2
    l.sort()
    i=0
    c=0
        

    if (m>=1):

        while(i!=m):
            
            l1=[]
            l1.append(l[i])
            
            for j in range(i+1,len(l)):
                if(l[j]%l[i]==0):
                    l1.append(l[j])
                    
                    for k in range (j+1,len(l)):
                        
                        if(l[k]%l[j]==0):
                            l1.append(l[k])

                            c += 1
                            
                            print(l1)
                            
                            l1.remove(l[k])
                        
                    l1.remove(l[j])
        
            i += 1
            
    return c
