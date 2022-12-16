import view
import model
import parser
import logger

def input_formula():
    parser.reset_error()
    tips=''
    if not parser.get_formulaString()=='':
        tips=parser.get_formulaString()
        model.set_first(int(parser.get_formulaString()))
    if not model.get_first()==None:
        tips=model.get_first()
        parser.set_first(str(model.get_first()))
    string=view.input_formula(tips)
    parser.set_formulaStringFromInput(f'{tips}{string}')
    if string.isdigit() or string in ['+','-','*','/']:
        if string.isdigit():
            input_first(int(string))
        else:

            input_operation(string)

        return False
    else:
        parser.set_formulaString(string)
        return True




def input_first(number=None):
    if number==None:
        number=view.input_number()
    model.set_first (number)

def input_second():
    while True:
        number=view.input_number (str(model.get_first())+str(model.get_operation()))
        if model.get_operation() =='/' and number==0:
            view.print_divizion_by_zero()
        else:
            model.set_second(number)
            break

def input_operation(oper=''):
    if oper=='':
        oper=view.input_operation(model.get_first())
    if model.get_operation()=='':
        model.set_operation(oper)
def solution_formula():
    operations=parser.get_operation()
    numbers=parser.get_numbers()
    while (len(operations)>0):
        if '*' in operations:
            parser.multiplication(operations.index('*'))
        elif '/' in operations:
            parser.division(operations.index('/'))
        elif '-' in operations and parser.get_error()=='':
            parser.difference(operations.index('-'))
        elif '+' in operations and parser.get_error()=='':
            parser.addition(operations.index('+'))
    if parser.getHesSteples():
        parser.killSteples()
    elif parser.get_error()=='':
        result_string = f'{parser.get_formulaStringFromInput()}={parser.get_result()}'
        view.print_to_console(result_string)
        logger.writeToLog(result_string)
        model.set_first(parser.get_result())
        parser.set_first(parser.get_result())
        model.set_operation('')


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

    result_string=f'{model.get_first()}{model.get_operation()}{model.get_second()}={model.get_result()}'
    view.print_to_console(result_string)
    logger.writeToLog(result_string)
    model.set_first(model.get_result())
    model.set_operation('')
    parser.set_first(model.get_result())

def start():
    while True:
        if input_formula():
            while (parser.checkSteples()):
                if parser.Steples():
                    if (parser.getFormula(parser.get_formulaString())):
                        solution_formula()
            if parser.get_error() == '':
                if (parser.getFormula(parser.get_formulaString())):
                    solution_formula()
                    if parser.get_finish():
                        view.log_off()
                        break
            if not (parser.get_error()==''):
                view.print_error(parser.get_error())
        elif parser.get_error()=='':
            input_operation(model.get_operation())
            if model.get_operation() =='=':
                view.log_off()
                break
            input_second()
            solution()

