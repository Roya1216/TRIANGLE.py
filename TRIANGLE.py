print (' Please enter the three numbers you intend for the sides of your triangle az w ,t ,e :\n')
w=int(input())
t=int(input())
e=int(input())

if w+t>e:
    if w+e>t:
        if t+e>w:
            print("it's a triangle" )
            
else:
    print("it's not a triangle ")