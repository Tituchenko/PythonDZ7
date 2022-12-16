numbers=[]
operations=[]
formulaString=''
Error=''
Finish=False
StartSteples=0
EndSteples=0
hasSteples=False
formulaStringFull=''
formulaStringFromInput=''

def reset_error(): # сбросим ошибки
    global Error
    Error=''

def getHesSteples():
    global hasSteples
    return hasSteples

def set_formulaStringFromInput(string):
    global formulaStringFromInput
    formulaStringFromInput=string

def get_formulaStringFromInput():
    global formulaStringFromInput
    return formulaStringFromInput

def Steples(): # загружаем в global индексы начала и конца скобок, проверяем корректность
    global formulaString
    global formulaStringFull
    global Error
    global hasSteples
    StartSteples=0
    EndSteples=len (formulaString)
    for i,s in enumerate(formulaString):
        if s=='(' and i>StartSteples:
            StartSteples=i
    try:
        EndSteples=formulaString.index(')',StartSteples)
    except:
        Error='Отсутсвует закрывающая скобка'
        hasSteples=False
        formulaString=''
        return False
    if StartSteples>EndSteples:
        Error='Некорректные скобки'
        formulaString=''
        hasSteples=False
        return False
    if StartSteples>0:
        if formulaString[StartSteples-1] not in ['+','-','*','/','(',')']:
            Error = f'Перед скобкой долен стоять знак! а не {formulaString[StartSteples-1]}'
            formulaString = ''
            hasSteples = False
            return False
    if EndSteples<(len(formulaString)-1):
        if formulaString[EndSteples+1] not in ['+','-','*','/','(',')','=']:
            Error = f'После скобкой долен стоять знак! а не {formulaString[EndSteples+1]}'
            formulaString = ''
            hasSteples = False
            return False



    formulaStringFull=formulaString
    formulaString=formulaString[StartSteples+1:EndSteples]
    return True


def checkSteples(): # А есть ли скобки в формуле вообще, проверяем чтобы обе
    global formulaString
    global hasSteples
    if '(' in formulaString:
        hasSteples=True
        return True
    else:
        hasSteples = False
        return False

def get_finish():
    global Finish
    return Finish

def get_error():
    global Error
    return Error

def set_first(number):
    global formulaString
    global numbers
    formulaString = str(number)
    numbers.clear()

def set_formulaString(s: str):
    global formulaString
    formulaString+=s


def get_result():
    global numbers
    return numbers[0]

def killSteples(): # меняем в строке то что в скобках на значение
    global formulaString
    global formulaStringFull
    global numbers
    formulaString=formulaStringFull.replace(f'({formulaString})',str(get_result()))
    formulaStringFull=''
    numbers.clear()

def get_formulaString():
    global formulaString
    return formulaString

def get_numbers():
    global numbers
    return numbers

def get_operation():
    global operations
    return operations

def addNumber(num):
    global numbers
    if not num=='':
        numbers.append(int(num))

def cleanFormula(f:str) -> str:
    f=f.replace(' ','')
    f=f.replace('+-', '-')
    f=f.replace('--', '+')
    f=f.replace('++', '+')
    return f

def reset_numbers(): #сбросим значения только не 0 - там обычно храниться результат прошлых вычислений
    global numbers
    global operations
    operations.clear()
    temp=None
    if len(numbers)>0:
        temp=numbers[0]
    numbers.clear()
    if not temp==None:
        numbers.append(temp)

def getFormula(formula : str): # разобьем строку на два списка - операции и элементы, небольшие проверки корректности
    global operations
    global Error
    global Finish
    global formulaString
    global formulaStringFromInput
    curNumber=''
    symbolBefore=''
    formula=cleanFormula(formula)
    for i,s in enumerate(formula):
        if s.isdigit():
            curNumber+=s
        elif s=='-':
            if symbolBefore in ['*','/','']:
                curNumber += s
            else:
                operations.append(s)
                addNumber(curNumber)
                curNumber = ''
        elif s in ['+','*','/']:
            operations.append(s)
            addNumber(curNumber)
            curNumber=''
        elif s =='=':
            if i==(len(formula)-1):
                Finish=True
                addNumber(curNumber)
                formulaStringFromInput=formulaStringFromInput[0:formulaStringFromInput.index('=')]
                return True
            else:
                Error = 'Равно должно быть в конце!'
                formulaString = ''
                reset_numbers()
                return False
        else:
            Error=f'Неокректный символ "{s}"в выражении {formulaStringFromInput}'
            formulaString=''
            reset_numbers()
            return False
        symbolBefore = s
    addNumber(curNumber)

    return True

def multiplication(i:int):
    global numbers
    global operations
    numbers[i]=numbers[i]*numbers[i+1]
    del (numbers[i+1])
    del (operations[i])

def division(i:int):
    global numbers
    global operations
    global formulaString
    global Error
    if not (numbers[i+1]==0):
        numbers[i]=numbers[i]/numbers[i+1]
        if numbers[i] == int(numbers[i]):
            numbers[i] = int(numbers[i])
        del (numbers[i + 1])
        del (operations[i])
    else:
        Error='На ноль делить нельзя'
        formulaString = ''
        reset_numbers()


def addition(i:int):
    global numbers
    global operations
    numbers[i]=numbers[i]+numbers[i+1]
    del (numbers[i+1])
    del (operations[i])

def difference(i:int):
    global numbers
    global operations
    numbers[i]=numbers[i]-numbers[i+1]
    del (numbers[i+1])
    del (operations[i])

