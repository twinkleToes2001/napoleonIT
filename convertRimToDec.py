# Римские цифры представлены в виде I, V, X, L, C, D и M
# Необходимо с помощью кода python преобразовать римское число
# в арабское (стандартное) число.
#
# Условия:
# 1. Длина 1 <= s.length <= 15
# 2. s состоит только из ('I', 'V', 'X', 'L', 'C', 'D', 'M')
# 3. Гарантируется, что конвертируемая в число s будет в диапозоне [1, 3999]

"""Реализация перевода римских чисел в арабские"""


class Solution:
    """Класс для реализации решения."""

    # Сюда записывается объяснение
    # при переводе числа
    explanation = ''

    # counter используется при выводе решения,
    # в функции print_solution()
    counter = 0

    # Не ясно зачем вообще использовать класс
    # Сразу скажу, что скорее всего не понял,
    # что вы имели ввиду, когда дали написать
    # решение на основе уже какого-то кода.
    # Поэтому я сделал два решения, одно,
    # как я понял, а другое - как бы я сделал.
    def romanToInt(self, _s: str) -> int:
        """Перевод римского числа в арабское"""
        ans, temp, result = 0, 0, 0
        self.explanation, letter = '', ''

        for symbol in _s:
            # Со <switch> это бы смотрелось гораздо приятнее!
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
                # Знаю, что строка гарантированно является правильной,
                # и это условие никогда не будет выполняться, но если
                # бы я написал <else> заместо кейса <elif symbol == 'M'>,
                # то это ухудшило бы читаемость и общую наглядность, ИМХО.
                # С другой стороны, как-то семантически не правильно,
                # с моей стороны, оставлять такую конструкцию без <else>,
                # поэтому был написан такой кейс =)
                return -1

            if ans <= temp:
                result += ans
                self.explanation += f'{letter} = {ans}, '
            else:
                result += ans - 2 * temp
                # Ужасно сложное выражение для корректрой генерации объяснения :0
                self.explanation = \
                    self.explanation.strip()[:-(4 + len(str(temp))):] + \
                    f'{letter} = {ans - temp}, '
            temp = ans
        # Обрезаем последнюю запятую, с помощью slice,
        # у explanation и ставим точку
        self.explanation = self.explanation.strip()[:-1:] + '.'
        return result

    def print_solution(self, _input, explanation=False):
        """Функция для печати в конслоль дынных конвертирования"""
        self.counter += 1
        _solution = f'Пример {self.counter}:\n' + \
                    f'Input: s = "{_input}"\n' + \
                    f'Output: {self.romanToInt(_input)}\n'
        # Тернарный оператор
        _solution += f'Explanation: {self.explanation}\n' if explanation else ''
        print(_solution)


if __name__ == '__main__':
    # Создаем экземпляр класса, без этого никак
    solution = Solution()

    # case 1:
    # Input: s = "III"
    # Output: 3
    s = 'III'
    solution.print_solution(s)

    # case 2:
    # Input: s = "IV"
    # Output: 4
    s = 'IV'
    solution.print_solution(s)

    # case 3:
    # Input: s = "IX"
    # Output: 9
    s = 'IX'
    solution.print_solution(s)

    # case 4:
    # Input: s = "LVIII"
    # Output: 58
    # Explanation: L = 50, V = 5, III = 3.
    s = 'LVIII'
    solution.print_solution(s, explanation=True)

    # case 5:
    # Input: s = "MCMXCIV"
    # Output: 1994
    # Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
    s = 'MCMXCIV'
    solution.print_solution(s, explanation=True)
