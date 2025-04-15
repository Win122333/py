class Student:
    def __init__(self, FIO, mark_rus, mark_math, mark_ph):
        self.FIO = FIO
        self.mark_rus = mark_rus
        self.mark_math = mark_math
        self.mark_ph = mark_ph

    def __str__(self):
        return f"{self.FIO} русский: {self.mark_rus}, математика: {self.mark_math}, физика: {self.mark_ph}"

    def __lt__(self, other):
        sum_self = int(self.mark_rus) + int(self.mark_math) + int(self.mark_ph)
        sum_other = int(other.mark_rus) + int(other.mark_math) + int(other.mark_ph)

        if sum_self != sum_other:
            return sum_self < sum_other
        else:
            if int(self.mark_math) != int(other.mark_math):
                return int(self.mark_math) < int(other.mark_math)
            else:
                return int(self.mark_ph) < int(other.mark_ph)