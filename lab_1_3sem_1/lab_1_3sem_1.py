import math
import sys

class BiSquare:
    def __init__(self):
        self.coef_A = 0.0
        self.coef_B = 0.0
        self.coef_C = 0.0
        self.num_roots = 0
        self.roots_list = []
        
    def get_coef(self, index, prompt):
        try:
            coef_str = sys.argv[index]
        except:
            print(prompt)
            coef_str = input()
        while True:
            try:
                coef = float(coef_str)
                break
            except:
                print('Ошибка: введено не число. Повторите ввод коэффициента.')
                coef_str = input()
 
        return coef
    
    def get_coefs(self):
        self.coef_A = self.get_coef(1, 'Введите коэффициент А:')
        self.coef_B = self.get_coef(2, 'Введите коэффициент B:')
        self.coef_C = self.get_coef(3, 'Введите коэффициент C:')
        
    def calculate_roots(self):
        pre_roots = []
        a = self.coef_A
        b = self.coef_B
        c = self.coef_C
        D = b*b - 4*a*c
        if a == 0.0:
            pre_roots.append(-c/b)
        elif D == 0.0:
            pre_roots.append(-b / (2.0 * a))
        elif D > 0.0:
            sqD = math.sqrt(D)
            pre_roots.append((-b + sqD) / (2.0*a))
            pre_roots.append((-b - sqD) / (2.0*a))
        for pre_root in pre_roots:
            if pre_root == 0:
                self.num_roots += 1
                self.roots_list.append(pre_root)
            elif pre_root > 0:
                self.num_roots += 2
                self.roots_list.append(math.sqrt(pre_root))
                self.roots_list.append(-math.sqrt(pre_root))
                
    def print_roots(self):
        if self.num_roots != len(self.roots_list):
            print(('Ошибка. Уравнение содержит {} действительных корней, ' +\
            'но было вычислено {} корней.').format(self.num_roots, len(self.roots_list)))
        else:
            if self.num_roots == 0:
                print('Нет корней')
            elif self.num_roots == 1:
                print('Один корень: {}'.format(self.roots_list[0]))
            elif self.num_roots == 2:
                print('Два корня: {} и {}'.format(self.roots_list[0], self.roots_list[1]))
            elif self.num_roots == 3:
                print('Три корня: {}, {} и {}'.format(roots[0], roots[1], roots[2]))
            elif self.num_roots == 4:
                print('Четыре корня: {}, {}, {}, и {}'.format(roots[0], roots[1], roots[2], roots[3]))
        
def main():
    r = BiSquare()
    r.get_coefs()
    r.calculate_roots()
    r.print_roots()

if __name__ == "__main__":
    main() 
