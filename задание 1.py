import math

f = open('in.txt','r')
N = int(f.readline())
M = int(f.readline(2))
H = int(f.readline(3))
f.close()
if (1 <= N <= H<=100) and (1 <= M <= 100):
    Q = math.ceil(M/(math.floor(H/N)))
    fil = open('out.txt','w')
    fil.write(str(Q))
    fil.close()
else:
    fil = open('out.txt','w')
    fil.write("Вас повесят через 3 дня, так как вы не сможете построить частокол")
    fil.close()
