def triangle(h):
    hauteur=h
    nbet=1
    nbes=hauteur-1
    for i in range(h):
        print(" "*nbes+"*"*nbet)
        nbes-=1
        nbet+=2
print(triangle(25))
