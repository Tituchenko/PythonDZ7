first_number=None
second_number=None
operation=''
result=0

def get_first():
    global first_number
    return first_number

def get_second():
    global second_number
    return second_number

def get_operation():
    global operation
    return operation

def get_result():
    global result
    return result

def set_first(value):
    global first_number
    first_number=value

def set_second(value):
    global second_number
    second_number=value

def set_operation(oper):
    global operation
    operation=oper

def addition():
    global first_number
    global second_number
    global result
    result=first_number+second_number

def difference():
    global first_number
    global second_number
    global result
    result=first_number-second_number

def multiplication():
    global first_number
    global second_number
    global result
    result=first_number*second_number

def division():
    global first_number
    global second_number
    global result
    result=first_number/second_number
    if result==int (result):
        result=int(result)