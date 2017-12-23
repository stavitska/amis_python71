def u(a, b):
    if a>0:
        b.append(int(input('input element: ')))
        u(a-1, b)
    else:
        return b
def i(a, b_1, b_2 ):
    if a>0:
        b_2.append(b_1[a-1])
        i(a-1, b_1, b_2)
    else:
        return b_2

d_in=[]
d_out=[]

k=int(input('Input N: '))

u(k, d_in)
print(d_in)

i(k, d_in, d_out)
print(d_out)

input('Press enter')