def ten_dev(x):
    return 10 / x

#except ZeroDivisionError
try:
    ten_dev(0)
except:
    print('Error Occured', end='\n\n')


#Except Specific Error
data = [0, 10, 20, 30]

for _ in range(len(data)+1):
    try:
        ten_dev(data[_])
    except ZeroDivisionError:
        print('ZeroDivisionError Occured')
    except IndexError:
        print('IndexError Occured')
print()


#Except Check Error Message
try:
    ten_dev(0)
except ZeroDivisionError as e:
    print(e, end='\n\n')


#Except with else, finally
try:
    ten_dev(0)
except Exception as e:
    print(e)
else:
    print('No Error Occured')
finally:
    print('try clause Done')
print()


#Exception raise
try:
    x = 1
    if type(x) != str():
        raise Exception('Use appropriate type')
    print('test next print')
except Exception as e:
    print('Out Exception', e, end='\n\n')


def type_match():
    try:
        x = 1
        if type(x) != str():
            raise Exception('Use appropriate type')
    except Exception as e:
        print('Error Occured in type: ', e)
        raise RuntimeError('Runtime Error Occured')

try:
    type_match()
except Exception as e:
    print(e, end='\n\n')


#Exception Create
class NewException(Exception):
    def __init__(self):
        super().__init__('Error Message')

class SecException(Exception):
    pass


def test_newException():
    try:
        x = 1
        if type(x) != str():
            raise NewException
    except Exception as e:
        print(e)
        raise SecException('SecException Occured')

try:
    test_newException()
except Exception as e:
    print(e)







































#
