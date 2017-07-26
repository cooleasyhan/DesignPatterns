class A: pass

class B: pass

class C(A,B):
     pass

print(C.mro())
c = C()
print(super(C))
print(type(super(C,c)))