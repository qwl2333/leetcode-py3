'''
https://www.1point3acres.com/bbs/thread-1066293-1-1.html
给一个class有三个iterator，像round robin一样遍历这三的iterator，每次返回一个数值
'''
class LetterNumberIterator:
    def __init__(self, letter, max_value):
        self.letter = letter
        self.max_value = max_value
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.max_value:
            raise StopIteration
        else:
            result = f"{self.letter}{self.current}"
            self.current += 1
            return result

    def has_next(self) -> bool:
        if self.current <= self.max_value:
            return True
        else:
            return False

# a_iterator = LetterNumberIterator('a', 5)
# a_it = iter(a_iterator)
# print(next(a_it))
# print(next(a_it))
# print(next(a_it))
# print(next(a_it))
# print(next(a_it))
# print(next(a_it, None)) # iterator exausted, instead of raising StopIteration

class RoundRobinIterators:
    def round_robin_three_iterators(self, a_it: LetterNumberIterator, b_it: LetterNumberIterator, c_it: LetterNumberIterator):
        iterators = [a_it, b_it, c_it]
        i = 0
        while a_it.has_next() or b_it.has_next() or c_it.has_next():
            cur_it = iterators[i]
            print(cur_it.has_next())
            i = (i + 1) % 3
            if not cur_it.has_next():
                continue
            print(next(cur_it))


a_iterator = LetterNumberIterator('a', 5)
b_iterator = LetterNumberIterator('b', 5)
c_iterator = LetterNumberIterator('c', 5)
rb_its = RoundRobinIterators()
rb_its.round_robin_three_iterators(a_iterator, b_iterator, c_iterator)
