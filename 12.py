# # modules - libraries 
# import math as m

# # print(m.e)
# # help(m)
# # print(dir(m))


# Making User made module

import example as ex
# from example import add

x,y = 4,2

# # add
# ans = add(x,y)
# print(ans)

# sub   
ans = ex.sub(x,y)
print(ans)

# div
ans = ex.div(x,y)
print(ans)

# multiply
ans = ex.mult(x,y)
print(ans)


# print(dir(ex))


# 1 function inside another 

# def fun1():
#     x=1
#     print(x)

#     def fun2():
#         x=2
#         print(x)

#     fun2()

# fun1()


print(__name__)
# if __name__ == "__main__"