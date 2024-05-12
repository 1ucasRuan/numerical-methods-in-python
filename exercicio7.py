import sys
from scipy.optimize import linprog

input_file = "exercicio7in.txt"
output_file = "exercicio7out.txt"
data = []


if len(sys.argv)>1 :
    input_file = sys.argv[1]
if len(sys.argv)>2 :
    output_file = sys.argv[2]

with open(input_file,'r') as f:
    for line in f:
        tokens = line.split()
        if len(tokens)<1 :
            continue
        dataItem = []
        for token in tokens:
            dataItem.append(float(token))
        data.append(dataItem)

print(data)

obj = data[0]
lhs = data[1:-1]
rhs = data[-1]
bnd = []

for k in obj :
    bnd.append( (0,float('inf')) )
 
o = linprog(c=obj, A_ub=lhs, b_ub=rhs, bounds=bnd, method='highs')

with open(output_file,'w') as f :
    for x in o.x :
        f.write(f'{x} ')
    f.write('\n')
