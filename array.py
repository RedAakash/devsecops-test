class ArrayIntersect:
    def __init__(self, arr1, arr2):
        self.arr1 = arr1
        self.arr2 = arr2

    def get_common(self):
        i, j = 0, 0
        result = []
        while i < len(self.arr1) and j < len(self.arr2):
            if self.arr1[i] == self.arr2[j]:
                if not result or result[-1] != self.arr1[i]:
                    result.append(self.arr1[i])
                i += 1
                j += 1
            elif self.arr1[i] < self.arr2[j]:
                i += 1
            else:
                j += 1
        return result

if __name__ == "__main__":
    a = [1, 2, 2, 3, 5, 7]
    b = [2, 2, 3, 4, 7, 8]
    intersector = ArrayIntersect(a, b)
    print("Common elt:", intersector.get_common())
