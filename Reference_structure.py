
x = [1, 2, 3]
y = [100, x, 120]
z = [x ,'a', 'b']

print(x, y, z)

x[1] = 1717 ; print(x, y, z) 
""" x 값이 바뀌면서, y, z 안에 있는 x(x가 reference하는 값)도 변하게 된다"""


x[1] = 2
x2 = [1,2,3]

x == x2 # True, 두 object의 value가 같으므로

x is x2 # False, 두 object의 reference 다르므로