def solution(n):

    c=0
    n = int(n)
    while(n!=1):

        if(n%2==0):
                n=n/2
        else:
            if ((n+1)/2)%2==0 and n!=3:
                n=n+1
            else:
                n=n-1
        
        c += 1

    return c
