def isPrime(self,N):
        # code here
        if(N==1):
            return False
        count=0
        for i in range(2,int(N**(0.5))+1,1):
            if(N%i==0):
                count+=1
        if(count==0):
            return True
        else:
            return False
