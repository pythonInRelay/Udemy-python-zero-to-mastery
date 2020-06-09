# MRO - Method Resolution Order
# How Python decices what to run first


class A:
    num = 10


class B(A):
    pass


class C(A):
    num = 1


class D(B, C):
    pass


print(D.num)
print(D.mro())

# Order they will be run in = D -> B -> C -> A

#       A
#      / \
#     /   \
#    B     C   # B & C inherit from A
#     \   /
#      \ /
#       D    # D inherits from B & C (and A)
