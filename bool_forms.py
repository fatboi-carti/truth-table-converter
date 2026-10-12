##def sub(number):
##    sub_digits = {"0": "₀", "1": "₁", "2": "₂", "3": "₃", "4": "₄", 
##                        "5": "₅", "6": "₆", "7": "₇", "8": "₈", "9": "₉"}
##    return "".join(sub_digits[digit] for digit in str(number))
##
##def pdnf(v_set, v_cnt):
##    b_set = f"{v_set:0{v_cnt}b}"
##    pdnf_elem = ""
##    for n in range(v_cnt):
##        if b_set[n] == '0':
##            pdnf_elem += f"x\u0304{sub(n)}"
##        else:
##            pdnf_elem += f"x{sub(n)}"
##    return pdnf_elem
##
##def pcnf(v_set, v_cnt):
##    b_set = f"{v_set:0{v_cnt}b}"
##    pcnf_elem = ""
##    for n in range(v_cnt):
##        if b_set[n] == '1':
##            if n == 0:
##                pcnf_elem += f"x\u0304{sub(n)}"
##            else:
##                pcnf_elem += f"∨x{sub(n)}"
##        else:
##            if n == 0:
##                pcnf_elem += f"x{sub(n)}"
##            else:
##                pcnf_elem += f"∨x{sub(n)}"
##    return pcnf_elem
##
##def pj(v_set, v_cnt, coef):
##    b_set = f"{v_set:0{v_cnt}b}"
##    pj_elem = ""
##    if v_set == 0:
##        pj_elem += '1'*coef[0]
##        return pj_elem
##    for n in range(v_cnt):
##        if b_set[n] == '1':
##            pj_elem += f"x{sub(n)}"
##    return pj_elem
##
##
##isValid_count = False
##
##while isValid_count == False:
##    try:
##        var_count = int(input("Введите количество переменных: "))
##        isValid_count = True
##    except (TypeError, ValueError):
##        print("Неправильный ввод.\n")
##
##
##isValid_func = False
##
##while isValid_func == False:
##    print(f"Введите двоичное значение функции по таблице истинности. {2**var_count} элементов (0,1)\n")
##
##    func = input()[:(2**var_count)]
##
##    funcElems = set(func)
##    sideElems = [x for x in funcElems if x not in "01"]
##    
##    if len(sideElems) > 0:
##        print("Введены недопустимые знаки.\n")
##
##    elif len(func) < 2**var_count:
##        print("Меньше символов, чем нужно\n")
##
##    else:
##        isValid_func = True
##        print(f"Введённая функция:\n{func[:(2**var_count)]}\n")
##
##
##resultD = ""
##
##for i in range(0, 2**var_count):
##    if func[i] == '1':
##        if resultD == "":
##            resultD += f"{pdnf(i, var_count)}"
##        else:
##            resultD += f" ∨ {pdnf(i, var_count)}"
##
##resultC = ""
##
##for i in range(0, 2**var_count):
##    
##    if func[i] == '0':
##        resultC += '('
##        resultC += f"{pcnf(i, var_count)}"
##        resultC += ')'
##        
##resultP = ""
##funcPJ = [int(x) for x in func]
##coefficients = [funcPJ[0]]
##
##n = len(funcPJ)
##for i in range(n - 1):
##    for j in range(n - 1, i, -1):
##        funcPJ[j] = funcPJ[j] ^ funcPJ[j - 1]
##    coefficients.append(funcPJ[i + 1])
##
##for i in range(0, 2**var_count):
##    if coefficients[i] == 1:
##        if resultP == "":
##            resultP += f"{pj(i, var_count, coefficients)}"
##        else:
##            resultP += f" ⊕ {pj(i, var_count, coefficients)}"
##
##
##print(f"СДНФ: {resultD}\n")
##print(f"СКНФ: {resultC}\n")
##print(f"Полином Жегалкина: {resultP}\n")
##print(coefficients)
##input()
##


class App:

    def __init__(self):
        self.var_count = None
        self.func = None

        self.start()

    def start(self):
        self.input_data()
        self.convert()
        self.loop()

    def input_data(self):
        print("Ввод данных...\n")
        def get_var_count():
            is_valid_count = False

            while is_valid_count == False:
                try:
                    var_count = int(input("Введите количество переменных: "))
                    is_valid_count = True
                except (TypeError, ValueError):
                    print("Неправильный ввод.\n")
            return var_count

        def get_func(var_count):
            is_valid_func = False

            while is_valid_func == False:
                print(f"Введите двоичное значение функции по таблице истинности. {2**var_count} элементов (0,1)\n")

                func = input()[:(2**var_count)]

                func_elems = set(func)
                side_elems = [x for x in func_elems if x not in "01"]
                
                if len(side_elems) > 0:
                    print("Введены недопустимые знаки.\n")

                elif len(func) < 2**var_count:
                    print("Меньше символов, чем нужно\n")

                else:
                    is_valid_func = True
                    print(f"Введённая функция:\n{func[:(2**var_count)]}\n")
            return func

                
        
        self.var_count = get_var_count()
        self.func = get_func(self.var_count)

    def convert(self):

        def pdnf():
        def pcnf():
        def pj():

        
        print(f"СДНФ: {pdnf()}\n")
        print(f"СКНФ: {pcnf()}\n")
        print(f"Полином Жегалкина: {pj()}\n")
    
