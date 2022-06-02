itemsincart = 0

# 2 items will be added to cart

# if itemsincart != 2:
#    raise Exception('Product cart count not matching')

# if itemsincart != 2:
#    pass

# assert(itemising == 10)


# try :

"""
# in this try except we will get error message which we have printed
try:
    with open('test.txt', 'r') as reader:
        reader.read()
except:
    print('some how i reached this block because there is failure in try block')
"""


# In this try except block we will get error message which python give us
try:
    with open('test2.txt', 'r') as reader:
        reader.read()
except Exception as e:
    print(e)
finally:
    print('cleaning up resources')