def input_number(s='') -> int:
    while True:
        try:
            number=int(input(f'Введите целое число: {s}'))
            return number
        except:

            print ('Ошибка')

def input_operation(fisrtNumber=''):
    while True:
        operation=input (f'Введите операцию: {fisrtNumber}')
        if operation in ['+','-','*','/','=']:
            return operation
        else:
            print ('Введите корректную операцию')


def print_to_console (value_text):
    print (value_text)

def log_off():
    print ('До свидания!')

def print_divizion_by_zero():
    print ('На ноль делить нельзя!')


def input_formula(s) -> str:
    if s=='':
        text=f'Введите целое число или выражение: '
    else:
        text = f'Введите операцию или выражение: {s}'
    formula = input(text)
    return formula
def print_error(text):
    print(text)