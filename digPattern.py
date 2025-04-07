class DigPattern:
    def __init__(self, x, n):
        self.x = x
        self.n = n

    def check(self):
        if not isinstance(self.x, int) or not isinstance(self.n, int):
            raise ValueError("use nums only")
        if self.x < 0 or self.x > 9:
            raise ValueError("x in 0–9")
        if self.n <= 0:
            raise ValueError("eepeat count > 0")

    def calc(self):
        self.check()
        total = 0
        val = ""
        for _ in range(self.n):
            val += str(self.x)
            total += int(val)
        return total

if __name__ == "__main__":
    try:
        d = DigPattern(3, 4)
        print("Result:", d.calc())
    except ValueError as err:
        print("Err:", err)
