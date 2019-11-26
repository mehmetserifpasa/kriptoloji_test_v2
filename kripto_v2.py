import sys,random



a = 20
aa = 1
aaa = "a"

b = 40
bb = 2
bbb = "b"

c = 60
cc = 3
ccc = "c"

ç = 80
çç = 4
ççç = "ç"

d = 100
dd = 5
ddd = "d"

e = 120
ee = 6
eee = "e"


f = 140
ff = 7
fff = "f"

g = 160
gg = 8
ggg = "g"

ğ = 180
ğğ = 9
ğğğ = "ğ"

h = 200
hh = 10
hhh = "h"

ı = 220
ıı = 11
ııı = "ı"

i = 240
ii = 12
iii = "i"

j = 260
jj = 13
jjj = "j"

k = 280
kk = 14
kkk = "k"

l =300
ll = 15
lll = "l"

m = 320
mm = 16
mmm = "m"

n = 340
nn = 17
nnn = "n"

o = 360
oo = 18
ooo = "o"

ö = 380
öö = 19
ööö = "ö"

p = 400
pp = 20
ppp = "p"

r = 420
rr = 21
rrr = "r"

s = 440
ss = 22
sss = "s"

ş = 460
şş = 23
şşş = "ş"

t = 480
tt = 24
ttt = "t"

u = 500
uu = 25
uuu = "u"

ü = 520
üü = 26
üüü = "ü"

v = 540
vv = 27
vvv = "v"

y = 560
yy = 28
yyy = "y"

z = 580
zz = 29
zzz = "z"



alf = ["a","b","c","ç","d","e","f","g","ğ","h","ı","i","j","k","l","m","n","o","ö","p","r","s","ş","t","u","ü","v","y","z"]

text = "satranç"
sifre = []

for st in text:
    if st == aaa:
        if len(str(a)) == 2:
            sifre.append(random.choice(alf)+str(a)+random.choice(alf))


    if st == bbb:
        if len(str(b)) == 2:
            sifre.append(random.choice(alf)+str(b)+random.choice(alf))
        if len(str(b)) == 3:
            sifre.append(str(b) + random.choice(alf))


    if st == ccc:
        if len(str(c)) == 2:
            sifre.append(random.choice(alf) + str(c) + random.choice(alf))


    if st == ççç:
        if len(str(ç)) == 2:
            sifre.append(random.choice(alf) + str(b) + random.choice(alf))


    if st == ddd:
        if len(str(d)) == 3:
            sifre.append(str(b) + random.choice(alf))

    if st == eee:
        if len(str(e)) == 3:
            sifre.append(str(e) + random.choice(alf))
    if st == fff:
        if len(str(f)) == 3:
            sifre.append(str(f) + random.choice(alf))
    if st == ggg:
        if len(str(g)) == 3:
            sifre.append(str(g) + random.choice(alf))
    if st == ğğğ:
        if len(str(ğ)) == 3:
            sifre.append(str(ğ) + random.choice(alf))
    if st == hhh:
        if len(str(h)) == 3:
            sifre.append(str(h) + random.choice(alf))
    if st == ııı:
        if len(str(ı)) == 3:
            sifre.append(str(ı) + random.choice(alf))
    if st == iii:
        if len(str(i)) == 3:
            sifre.append(str(i) + random.choice(alf))
    if st == jjj:
        if len(str(j)) == 3:
            sifre.append(str(j) + random.choice(alf))
    if st == kkk:
        if len(str(k)) == 3:
            sifre.append(str(k) + random.choice(alf))
    if st == lll:
        if len(str(l)) == 3:
            sifre.append(str(l) + random.choice(alf))
    if st == mmm:
        if len(str(m)) == 3:
            sifre.append(str(m) + random.choice(alf))
    if st == nnn:
        if len(str(n)) == 3:
            sifre.append(str(n) + random.choice(alf))
    if st == ooo:
        if len(str(o)) == 3:
            sifre.append(str(o) + random.choice(alf))
    if st == ööö:
        if len(str(ö)) == 3:
            sifre.append(str(ö) + random.choice(alf))
    if st == ppp:
        if len(str(p)) == 3:
            sifre.append(str(p) + random.choice(alf))
    if st == rrr:
        if len(str(r)) == 3:
            sifre.append(str(r) + random.choice(alf))
    if st == sss:
        if len(str(s)) == 3:
            sifre.append(str(s) + random.choice(alf))
    if st == şşş:
        if len(str(ş)) == 3:
            sifre.append(str(ş) + random.choice(alf))
    if st == ttt:
        if len(str(t)) == 3:
            sifre.append(str(t) + random.choice(alf))
    if st == uuu:
        if len(str(u)) == 3:
            sifre.append(str(u) + random.choice(alf))
    if st == üüü:
        if len(str(ü)) == 3:
            sifre.append(str(ü) + random.choice(alf))
    if st == vvv:
        if len(str(v)) == 3:
            sifre.append(str(v) + random.choice(alf))
    if st == yyy:
        if len(str(y)) == 3:
            sifre.append(str(y) + random.choice(alf))
    if st == zzz:
        if len(str(z)) == 3:
            sifre.append(str(z) + random.choice(alf))
    else:
        pass



dosya = open("sifre.txt","w")
for sf in sifre:
    dosya.writelines(str(sf)+" ")
















