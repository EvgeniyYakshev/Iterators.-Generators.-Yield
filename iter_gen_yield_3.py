              # 1 вариант

##list_of_lists_2 = [
##        [['a'], ['b', 'c']],
##        ['d', 'e', [['f'], 'h'], False],
##        [1, 2, None, [[[[['!']]]]], []]
##        ]


class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.iterators_queue = []  # очередь
        self.current_iterator = iter(self.list_of_list)
        return self

    def __next__(self):
        while True:
            try:
                self.current_element = next(self.current_iterator)
                #  пытаемся получить следующий элемент
            except StopIteration:
                if not self.iterators_queue:
                    # если в текущем итераторе элементов не осталось и очередь иетраторов пуста
                    # завершаем цикл
                    raise StopIteration
                else:
                    # берем итератор из очереди
                    self.current_iterator = self.iterators_queue.pop()
                    continue
            if isinstance(self.current_element, list):
                # если следующий эелемент оказался списком, то
                # добавляем текущий итератор в очередь
                # а текущим итераторм делаем следующий элемент
                self.iterators_queue.append(self.current_iterator)
                self.current_iterator = iter(self.current_element)
            else:
                # если элемент не список, то просто возвращаем его
                return self.current_element
#for item in FlatIterator(list_of_lists_2):
    #print(item)            

def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()
                       # 2 вариант

##class FlatIteratorHard:
##
##    def __init__(self, list_of_list):
##        self.list_of_list = list_of_list
##
##    def __iter__(self):
##        self.iters_stack = [iter(self.list_of_list)]
##        return self
##
##    def __next__(self):
##        while self.iters_stack:
##            try:
##                next_item = next(self.iters_stack[-1])
##                #  пытаемся получить следующий элемент
##            except StopIteration:
##                self.iters_stack.pop()
##                #  если не получилось, значит итератор пустой
##                continue
##
##            if isinstance(next_item, list):
##                # если следующий элемент оказался списком, то
##                # добавляем его итератор в стек
##                self.iters_stack.append(iter(next_item))
##
##            else:
##                return next_item
##        raise StopIteration



##class FlatIterator:
##
##    def __init__(self, list_of_list):
##        # self.l_of_l = list_of_list[::-1]
##        self.list_of_list = list_of_list
##
##    def __iter__(self):
##        self.l_of_l = [iter(self.list_of_list)]
##        return self
##
##    def __next__(self):
##        # counter = 0
##        # length = len(self.l_of_l)
##        #
##
##
##        for element_ in self.l_of_l:
##            if isinstance(element_, list):
##              FlatIterator(element_)
##            else:
##                return element_

##list_of_lists_2 = [
##    [['a'], ['b', 'c']],
##    ['d', 'e', [['f'], 'h'], False],
##    [1, 2, None, [[[[['!']]]]], []]
##]
##
##my_iterator = FlatIteratorHard(list_of_lists_2)
##for element in my_iterator:
##    print(element)
