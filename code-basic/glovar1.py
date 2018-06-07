x = 'global value'

def func():
    
    x = 'local value'
    print('* inside function')
    print(x)

print('* before function')
print(x)
func()
print('* after function')
print(x)
