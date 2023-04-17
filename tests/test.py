a = int(input("a?: "))
b = int(input("b?: "))
c = int(input("c?: "))
d = int(input("d?: "))
e = int(input("e?: "))
f = int(input("f?: "))
g = int(input("g?: "))
h = int(input("h?: "))
i = int(input("i?: "))
j = int(input("j?: "))
k = int(input("k?: "))
l = int(input("l?: "))
m = int(input("m?: "))
n = int(input("n?: "))
o = int(input("o?: "))
p = int(input("p?: "))
q = int(input("q?: "))
r = int(input("r?: "))
s = int(input("s?: "))
t = int(input("t?: "))
u = int(input("u?: "))
v = int(input("v?: "))
w = int(input("w?: "))
x = int(input("x?: "))   
y = int(input("y?: "))
z = int(input("z?: "))

NamesOfVariables = {'a': a, 'b': b, 'c': c, 'd': d, 'e': e, 'f': f, 'g': g, 'h': h, 'i': i, 'j': j, 'k': k, 'l': l, 'm': m, 'n': n, 'o': o, 'p': p, 'q': q, 'r': r, 's': s, 't': t, 'u': u, 'v': v, 'w': w, 'x': x, 'y': y, 'z': z}

Answer = dict(sorted(NamesOfVariables.items(), key=lambda item: item[1], reverse=True)) #Sort The List From Greatest To Least

# Remove the last 20 items from the sorted dictionary
for i in range(21):
    Answer.popitem()

print(''.join(Answer.keys()))
