'''
inheritance allows a class(child/derived) to reuse properties & methods
of another class(parent/base)-- helps in code reusablity & method extension
'''
class A:
    def m1(self):
        print('m1 method from class A')

# single inheritance
class B(A): # B is deriving from class A
    def m2(self):
        print('m2 method from class B')

bobj = B()
bobj.m1()
bobj.m2()

# ****************** single inheritance eg 2****************************
class A1:
    x, y = 2, 20
    def m1(self):
        print(self.x + self.y)

class B1(A1):
    a, b = 100, 20
    def m2(self):
        print(self.a - self.b)

bobj = B1()
bobj.m1()
bobj.m2()

# ************* multi level inhertance ****************
class AA:
    x, y = 100, 200
    def m1(self):
        print(self.x + self.y)

class BB(AA):
    a, b = 1000, 200
    def m2(self):
        print(self.a - self.b)

class CC(BB):
    m,n = 10, 20
    def m3(self):
        print(self.m * self.n)

ccobj = CC()
ccobj.m1()
ccobj.m2()
ccobj.m3()

# ************* hierarchical inheritance - 1parent multiple childs **************
class AAA:
    x, y = 100, 200
    def m1(self):
        print(self.x + self.y)

class BBB(AAA):
    a, b = 100, 20
    def m2(self):
        print(self.a - self.b)

class CCC(AAA):
    i, j = 10, 20
    def m3(self):
        print(self.i * self.j)

bbbobj = BBB()
bbbobj.m1()
bbbobj.m2()

cccobj = CCC()
cccobj.m1()
cccobj.m3()

# ************ multiple inheritance [multiple parent - one child]******************
class P1:
    x, y = 100, 200
    def m1(self):
        print(self.x + self.y)

class P2:
    m, n = 200, 100
    def m2(self):
        print(self.m - self.n)

class C1(P1, P2): # multiple parents - not possible in Java
    i, j = 10, 20
    def m3(self):
        print(self.i * self.j)

c1obj = C1()
c1obj.m1()
c1obj.m2()
c1obj.m3()

#*******************************************************************************
# method overriding -- run time polymorphism
class Cl1:
    def m1(self):
        print('m1 method from class Cl1')

class Cl2(Cl1):
    def m1(self):
        print('m1 method overriden in class Cl2')
        super().m1() # invoke parent m1 using super keyword

cl2obj = Cl2()
cl2obj.m1() # m1 method overriden in class Cl2
# if we want ot access m1 from parent, then use super keyword 
'''output of cl2obj.m1() will be-
m1 method overriden in class Cl2
m1 method from class Cl1
'''

# calling parent class variables in child class
class ABCD:
    a, b= 10, 20

class EFGH(ABCD):
    i,j = 100, 200
    def m1(self, x, y):
        print('Inside EFGH, local variables',x + y)
        print('EFGH class variables', self.i + self.j)
        print('EFGH inherited variables from class ABCD',self.a + self.b)

efghobj = EFGH()
efghobj.m1(100, 200)
print(efghobj.a)
print(efghobj.b)
print(efghobj.i)
print(efghobj.j)

# ******* overriding variable************
class Par:
    name = 'scott'
class Chi(Par):
    name = 'John'
    def m1(self):
        print(super().name)
chiobj = Chi()
print(chiobj.name) # John
chiobj.m1() # scott

# ********* more overriding ***************
class Bank:
    def rate_of_interest(self):
        return 0

class Xbank(Bank):
    def rate_of_interest(self):
        return 10.5

class Ybank(Bank):
    def rate_of_interest(self):
        return 12.5

xbankobj = Xbank()
print(xbankobj.rate_of_interest()) # 10.5
ybankobj = Ybank()
print(ybankobj.rate_of_interest()) # 12.5

#***************************************************************************
