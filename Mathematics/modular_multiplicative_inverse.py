def modInverse(self,a,m):
        ##Your code here
        for i in range(1,m+1,1):
            if((i*a)%m==1):
                return i
        return -1;
