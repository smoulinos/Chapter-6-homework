import turtle
tess = turtle.Turtle()
alex = tess
alex.color("hotpink")


a = [1, 2, 3]
b = a[:]
b[0]= 5



this = ["I", "am", "not", "a", "crook"]
that = ["I", "am", "not", "a", "crook"]
print("Test 1: {0}".format(this is that))
that = this
print("Test 2: {0}".format(this is that))



def scalar_mult(s,v):
    for i in range(len(v)):
        v[i] = v[i]*s
    return v

print(scalar_mult(5,[1,2]))
print(scalar_mult(3, [1, 0, -1]))



def replace(s, old, new):
    x = s.split(old)
    g = new
    new = g.join(x)
    return new

print(replace("Mississippi", "i", "I"))