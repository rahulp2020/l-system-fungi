class L_system:
    def __init__(self, axiom, rules):
        self.axiom = axiom
        self.rules = rules

    def generate(self, steps):
        result = self.axiom
        for _ in range(steps - 1):
            new_result = ''
            for char in result:
                if char in self.rules:
                    new_result += self.rules[char]
                else:
                    new_result += char
            result = new_result
        return result
def main():
    axiom = "AB"
    rules = {
        'A': 'A[B]',
        'B': 'B[C]',
        'C': 'C[A]'
    }
    l_system = L_system(axiom, rules)
    final_pattern = l_system.generate(4)
    print(final_pattern)
main()
