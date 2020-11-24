"""Реализация перевода римских чисел в арабские"""


class Roman:
    """Класс для реализации решения."""

    explanation = ''
    counter = 0

    def __init__(self, _s: str):
        self.number = _s

    def convert_rim_to_dec(self) -> int:
        """Перевод римского числа в арабское"""
        ans, temp, result = 0, 0, 0
        self.explanation, letter = '', ''

        for symbol in self.number:
            if symbol == 'I':
                ans = 1
                letter = symbol
            elif symbol == 'V':
                ans = 5
                letter = symbol
            elif symbol == 'X':
                ans = 10
                letter = symbol
            elif symbol == 'L':
                ans = 50
                letter = symbol
            elif symbol == 'C':
                ans = 100
                letter = symbol
            elif symbol == 'D':
                ans = 500
                letter = symbol
            elif symbol == 'M':
                ans = 1000
                letter = symbol
            else:
                return -1

            if ans <= temp:
                result += ans
                self.explanation += f'{letter} = {ans}, '
            else:
                result += ans - 2 * temp
                self.explanation = \
                    self.explanation.strip()[:-(4 + len(str(temp))):] + \
                    f'{letter} = {ans - temp}, '
            temp = ans
            
        self.explanation = self.explanation.strip()[:-1:] + '.'
        return result

    def print_solution(self, explanation=False):
        """Функция для печати в конслоль дынных конвертирования"""
        self.counter += 1
        _solution = f'Пример {self.counter}:\n' + \
                    f'Input: s = "{self.number}"\n' + \
                    f'Output: {self.convert_rim_to_dec()}\n'
        _solution += f'Explanation: {self.explanation}\n' if explanation else ''
        print(_solution)


if __name__ == '__main__':

    # case 1:
    num = Roman('III')
    num.print_solution()

    # case 2:
    num = Roman('IV')
    num.print_solution()

    # case 3:
    num = Roman('IX')
    num.print_solution()

    # case 4:
    num = Roman('LVIII')
    num.print_solution()

    # case 5:
    num = Roman('MCMXCIV')
    num.print_solution()
