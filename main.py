class Number:
    def __init__(self, value=0):
        self.value = value

    def set_value(self, value):
        self.value = value

    def get_value(self, value):
        return self.value

    def get_in_another_base(self, base):
        if base > 36:
            raise ValueError('Слишком большое счисления')
        alph = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        tmp = []
        number = self.value
        while number > base:
            tmp.append(alph[number % base])
            number //= base
        tmp.append(alph[number % base])
        return ''.join(reversed(tmp))


n = Number(152)
print(n.get_in_another_base(2))
print(n.get_in_another_base(8))
print(n.get_in_another_base(16))
print(n.get_in_another_base(23))