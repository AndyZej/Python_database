import math


def middle_elements(sequences):
    middle_elements = []
    for sequence in sequences:
        if len(sequence) != 0:
            middle_elements.append(sequence[len(sequence) // 2])

    return middle_elements


class SequenceOfNumbers:
    def __init__(self, start: int, stop: int, step: int):
        self.start = start
        self.stop = stop
        self.step = step


    def __len__(self):
        return math.ceil((self.stop - self.start) / self.step)

    def __getitem__(self, index):
        if index >= len(self) or index < 0:
            raise IndexError

        return self.start + index * self.step


a = SequenceOfNumbers(0, 0, 1)
print(len(a) // 2)


seq1 = SequenceOfNumbers(0, 0, 1)  # to be skipped
seq2 = SequenceOfNumbers(5, 15, 1)  # middle is 10
seq3 = SequenceOfNumbers(5, 15, 4)  # middle is 9
seq4 = SequenceOfNumbers(100, 201, 1)  # middle is 150
result = middle_elements([
            seq1
])
print(result)