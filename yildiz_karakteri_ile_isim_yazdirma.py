#21100011042/Nadire Nur/Sağlam

print("\n\nŞekillerin düzgün çıkması için lütfen boyutu tek sayı ve 3'den büyük giriniz. ")
boyut=int(input("Boyut giriniz: "))
print("\n\n")

#n harfi
for i in range(boyut):
     print("*", end=" ")

for i in range(boyut-1):
    if i == 0 :
        print(" ")
    print("*",(boyut-2)*"  ","*")
print("\n")

#u harfi
for i in range(boyut-1):
    if i == 0 :
       print(" ")
    print("*",(boyut-2)*"  ","*")
for i in range(boyut):
      print("*", end=" ")
print("\n\n")

#r harfi

bosluk=""
a=""
b=""
c=""
bs=""
for i in range(boyut): #yatay çizgiler
   b+="* "
print(b)
for i in range(boyut*2-3): #dikey çizgiler
    bosluk+=" "
a="*"+bosluk+"*"
for i in range(boyut//3):
    print(a)
print(b)
kalansatir=boyut//3+1
for i in range(kalansatir-4):
    bs+=" "
c="*"+bs+"*" #kuyruk
print(c)
kalansatir-=1
while kalansatir>0: #kuyruk
    bs+=" "
    c="*"+bs+"*"
    print(c)
    kalansatir-=1
