import sys
b = []
for i in range(57348):
    if (i > 55295):
        b.append(str("\\u"+str(i)))
with open(sys.argv[1], "r") as f:
    for line in f:
        for char in f:
            b.append(char)
for i in range(57348):
    if (i > 55295):
        b.append(str("\\u"+str(i)))
class get:
    x = lambda x: print(g.write(x), end="")
with open(sys.argv[2], "w") as g:
    (list(map(get.x, b)))

g.close()
f.close()