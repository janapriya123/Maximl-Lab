NO_OF_CHARS=256
def max_dist_char(str, n): 
	count=[0]*NO_OF_CHARS 
	for i in range(n): 
		count[ord(str[i])]+=1
	max_dist=0
	for i in range(NO_OF_CHARS): 
		if (count[i]!=0): 
			max_dist+=1	
	return max_dist 
def smallesteSubstr_maxDistictChar(str): 
	n=len(str)	
	max_dist=max_dist_char(str, n) 
	minl=n
	for i in range(n): 
		for j in range(n): 
			p=str[i:j] 
			p_len=len(p) 
			p_dist_char=max_dist_char(p,p_len) 
			if (p_len<minl and
				max_dist==p_dist_char): 
				minl=p_len 

	return minl 
if __name__=="__main__": 
	str=input("")
	l=smallesteSubstr_maxDistictChar(str); 
	print("smallest substring", 
		"consisting of maximum distinct", 
		"characters:",l) 


