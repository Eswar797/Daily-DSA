def digitsInFactorial(self,N):
        # code here
        fact=0
        for i in range(1,N+1):
            fact=fact+math.log(i,10)
        return int(fact)+1;
