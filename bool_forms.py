
class App:

    def __init__(self):
        self.var_count = None
        self.func = None

        self.start()

    def start(self):
        self.input_data()
        self.convert()
        self.loop()

    def loop(self):
        pass
    
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
        def sub(number):
            sub_digits = {"0": "₀", "1": "₁", "2": "₂", "3": "₃", "4": "₄", 
                                "5": "₅", "6": "₆", "7": "₇", "8": "₈", "9": "₉"}
            return "".join(sub_digits[digit] for digit in str(number))
        
        def b_set(v_set, v_cnt):
            return f"{v_set:0{v_cnt}b}"
        
        def pdnf(v_cnt, f):
            def pdnf_el(v_set, v_cnt):
                pdnf_elem = ""
                b = b_set(v_set, v_cnt)
                for n in range(v_cnt):
                    if b[n] == '0':
                        pdnf_elem += f"x\u0304{sub(n)}"
                    else:
                        pdnf_elem += f"x{sub(n)}"
                return pdnf_elem
                
            resultD = ""
            for i in range(0, 2**v_cnt):
                if f[i] == '1':
                    if resultD == "":
                        resultD += f"{pdnf_el(i, v_cnt)}"
                    else:
                        resultD += f" ∨ {pdnf_el(i, v_cnt)}"
            return resultD
            

        def pcnf(v_cnt, f):
            def pcnf_el(v_set, v_cnt):
                pcnf_elem = ""
                b = b_set(v_set, v_cnt)
                for n in range(v_cnt):
                    if b[n] == '1':
                        if n == 0:
                            pcnf_elem += f"x\u0304{sub(n)}"
                        else:
                            pcnf_elem += f"∨x{sub(n)}"
                    else:
                        if n == 0:
                            pcnf_elem += f"x{sub(n)}"
                        else:
                            pcnf_elem += f"∨x{sub(n)}"
                return pcnf_elem
            resultC = ""
            for i in range(0, 2**v_cnt):
    
                if f[i] == '0':
                    resultC += '('
                    resultC += f"{pcnf_el(i, v_cnt)}"
                    resultC += ')'
            return resultC
                
            
        def pj(v_cnt, f):
            def pj_coef(f):
                funcPJ = [int(x) for x in f]
                coef = [funcPJ[0]]
                n = len(funcPJ)
                for i in range(n - 1):
                    for j in range(n - 1, i, -1):
                        funcPJ[j] = funcPJ[j] ^ funcPJ[j - 1]
                    coef.append(funcPJ[i + 1])
                return coef
            
            def pj_el(v_set, v_cnt, coef):
                pj_elem = ""
                b = b_set(v_set, v_cnt)
                if v_set == 0:
                    pj_elem += '1'*coef[0]
                    return pj_elem
                for n in range(v_cnt):
                    if b[n] == '1':
                        pj_elem += f"x{sub(n)}"
                return pj_elem
                
            
            resultP = ""
            coefficients = pj_coef(f)
            for i in range(0, 2**v_cnt):
                if coefficients[i] == 1:
                    if resultP == "":
                        resultP += f"{pj_el(i, v_cnt, coefficients)}"
                    else:
                        resultP += f" ⊕ {pj_el(i, v_cnt, coefficients)}"
            return resultP
            
                

        
        print(f"СДНФ: {pdnf(self.var_count, self.func)}\n")
        print(f"СКНФ: {pcnf(self.var_count, self.func)}\n")
        print(f"Полином Жегалкина: {pj(self.var_count, self.func)}\n")
    
if __name__ == "__main__":
    App()
