def quadraticRoots(self, a, b, c):
        # code here
        d=b**2-4*a*c
        r1=(-b+((b**2-4*a*c)**(0.5)))/(2*a)
        r2=(-b-((b**2-4*a*c)**(0.5)))/(2*a)
        if(d<0):
            return [-1]
        else:
            if(math.floor(r1)>=math.floor(r2)):
                return [math.floor(r1),math.floor(r2)]
            else:
                return [math.floor(r2),math.floor(r1)]
