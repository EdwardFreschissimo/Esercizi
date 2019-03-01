import turtle as t
a = 0
b = 1
braccia = int(input("Inserisci il numero di braccia:"))
while True:
    if(braccia>0):
        t.forward(b)
        t.left(90)
        a, b = b, a + b
        braccia = braccia - 1
    else:
        break
t.done()



