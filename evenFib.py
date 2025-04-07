class EvenFib:
    def __init__(self, limit):
        self.limit = limit
        self.evens = []

    def generate(self):
        a, b = 0, 1
        while len(self.evens) < self.limit:
            nxt = a + b
            if nxt % 2 == 0:
                self.evens.append(nxt)
            a, b = b, nxt

    def get_sum(self):
        return sum(self.evens)

    def start(self):
        self.generate()
        print(f"Sum of first {self.limit} even fibo numbers: {self.get_sum()}")

if __name__ == "__main__":
    fib = EvenFib(100)
    fib.start()
