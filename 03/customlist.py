class CustomList(list):
    def __str__(self):
        elems = ""
        for i in self:
            elems += str(i) + " "
        return "Sum: " + str(sum(self)) + "\n" + "elements: " + elems

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)

    def __gt__(self, other):
        return sum(self) > sum(other)

    def __ge__(self, other):
        return sum(self) >= sum(other)

    def __ne__(self, other):
        return sum(self) != sum(other)

    def __sub__(self, other):

        min_len = min(len(self), len(other))
        max_len = max(len(self), len(other))

        result = CustomList([0] * max_len)

        for i in range(min_len):
            result[i] = self[i] - other[i]

        if min_len == max_len:
            return result
        if len(self) == max_len:
            for i in range(min_len, max_len):
                result[i] = self[i]
            return result
        for i in range(min_len, max_len):
            result[i] = -other[i]
        return result

    def __rsub__(self, other):

        min_len = min(len(self), len(other))
        max_len = max(len(self), len(other))

        result = CustomList([0] * max_len)

        for i in range(min_len):
            result[i] = other[i] - self[i]

        if min_len == max_len:
            return result
        if len(self) == max_len:
            for i in range(min_len, max_len):
                result[i] = -self[i]
            return result
        for i in range(min_len, max_len):
            result[i] = other[i]
        return result

    def __add__(self, other):
        min_len = min(len(self), len(other))
        max_len = max(len(self), len(other))

        result = CustomList([0] * max_len)

        for i in range(min_len):
            result[i] = other[i] + self[i]

        if min_len == max_len:
            return result
        if len(self) == max_len:
            for i in range(min_len, max_len):
                result[i] = self[i]
            return result
        for i in range(min_len, max_len):
            result[i] = other[i]
        return result

    def __radd__(self, other):
        min_len = min(len(self), len(other))
        max_len = max(len(self), len(other))

        result = CustomList([0] * max_len)

        for i in range(min_len):
            result[i] = other[i] + self[i]

        if min_len == max_len:
            return result
        if len(self) == max_len:
            for i in range(min_len, max_len):
                result[i] = self[i]
            return result
        for i in range(min_len, max_len):
            result[i] = other[i]
        return result
