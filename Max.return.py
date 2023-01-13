def max_return(x,y,z):
     if x>y and x>z:
         return x
     elif y>z:
         return y
     else:
         return z
print(max_return(4,17,12))
