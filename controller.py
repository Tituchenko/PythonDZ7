import view
import model

def input_first():
    number=view.input_number()
    model.set_first (number)

def input_second():
    while True:
        number=view.input_number ()
        if model.get_operation() =='/' and number==0:
            view.print_divizion_by_zero()
        else:
            model.set_second(number)
            break

def input_operation():
    oper=view.input_operation()
    model.set_operation(oper)

def solution():
    oper=model.get_operation()
    if oper=='+':
        model.addition()
    elif oper=='-':
        model.difference()
    elif oper=='*':
        model.multiplication()
    elif oper=='/':
        model.division()

    result_string=f'{model.get_first()} {model.get_operation()} {model.get_second()} = {model.get_result()}'
    view.print_to_console(result_string)
    model.set_first(model.get_result())

def start():
    input_first()
    while True:
        input_operation()
        if model.get_operation() =='=':
            view.log_off()
            break
        input_second()
        solution()