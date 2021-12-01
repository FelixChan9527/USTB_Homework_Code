def function(x):
    y = x*x - 6*x + 2
    return y

e = 0.03
F_8 = 89
F_7 = 55
a = 0
b = 10
# lam_2 = a + (F_7 / F_8) * (b-a)
# lam_1 = a + b - lam_2
lam_2 = a + 0.618 * (b-a)
lam_1 = a + 0.382*(b-a)
f1 = function(lam_1)
f2 = function(lam_2)
print("f1= ", f1, " f2=", f2)
k = 0


for i in range(8):
    if f2 > f1:
        b = lam_2
        lam_2 = lam_1
        lam_1 = a + b - lam_2
        f2 = f1
        f1 = function(lam_1)
        print("f2>f1", " l=", b-a, " lam1=", lam_1, " lam_2=", lam_2, " f1=", f1, " f2=", f2)
    else:
        a = lam_1
        lam_1 = lam_2
        lam_2 = a + b - lam_1
        f1 = f2
        f2 = function(lam_2)
        print("f2<f1", " l=", b-a, " lam1=", lam_1, " lam_2=", lam_2, " f1=", f1, " f2=", f2)
    # print("a=", a, " b=", b, " l=", b-a, " lam1=", lam_1, " lam_2=", lam_2)
    # print("f1= ", f1, " f2=", f2, " l=", b-a)
x_final = (a + b) / 2
y_final = function(x_final)
print("a=", a, " b=", b, " l=", b-a, " x*=", x_final, " y=", y_final)
