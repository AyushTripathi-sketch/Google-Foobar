def search(lis,n):

	for i in range(len(lis)):
		if lis[i]==n:
			return True
	return False




def solution(l):

	k=sum(l)        #sum of the digits of the list
	l.sort()        #sorting the list in ascending order
	s=""            #empty string for storing the output

	if k%3==0:      #condition for a no. being divisible by3
		
		l.sort(reverse=True)
		for i in l:
			s += str(i)
		return s

	elif k%3!=0 and len(l)>1 and k>=3:

		p=k//3

		while k%3!=0 and len(l)>1:

			r=k-3*p

			if r<=l[len(l)-1]:
				
				if search(l,r):
					l.remove(r)
					l.sort(reverse=True)
					for i in l:
						s += str(i)
					return s
					
				else :
					p=p-1
			else :
				l.remove(l[0])
				k=sum(l)
				p=k//3
		
		if len(l)==1 and l[0]%3==0:
			return l[0]
		else:
			return 0
	
	else:
		return 0

	
	
	



