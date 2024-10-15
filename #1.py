#1. Write a PYTHON program to evaluate the student performance

nilai = input("berapa nilai yang kamu peroleh : ") 
if int(nilai) >= 90:
    print ("exellent")

elif int(nilai) >= 80:
    print ("very good") 

elif int(nilai) >= 70:
    print ("good")

elif int(nilai) >=60:
    print ("you need to be better") 


#2.  Write a PYTHON program to find largest of three numbers!

def angka_terbesar(a,b,c):
    print("angka terbesarnya adalah : ", max (a, b, c)) 

a = int(input("masukkan angka ke-1 : ")) 
b = int(input("masukkan angka ke-2 : "))
c = int(input("masukkan angka ke-3 : "))

angka_terbesar(a,b,c) 


#3. Write a PYTHON program to print Fibonacci series up to n!

def fibonacci(n):
    a, b = 0, 1
    angka = []
    while a <= n:
        angka.append(a)
        a, b = b, a + b 
    print("angka fibonacci = ", angka) 

n = int(input("masukkan nilai n : "))
fibonacci(n)

#4. Write a PYTHON program to print odd numbers up to n!

def angka_ganjil(n):
    ganjil = [i for i in range(1, n + 1) if i % 2 != 0]
    print("Angka ganjil hingga n:", ganjil)

n = int(input("Masukkan nilai n: "))
angka_ganjil(n)


#5. Write a PYTHON program to produce pyramid design

def pyramid(n):
    for i in range(1, n + 1):
        print(str(i) * i)

n = int(input("Masukkan nilai n: "))
print("Angka yang dihasilkan:")
pyramid(n) 

