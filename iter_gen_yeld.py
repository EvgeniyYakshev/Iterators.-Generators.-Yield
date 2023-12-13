##list_of_lists_1 = [
##        ['a', 'b', 'c'],
##        ['d', 'e', 'f', 'h', False],
##        [1, 2, None]
##    ]



                          #1 вариант
class FlatIterator:

    def __init__(self, list_of_list):
        self.l_of_l = list_of_list

    def __iter__(self):
        self.index_1, self.index_2 = 0, 0
        return self

    def __next__(self):
        if self.index_1 == len(self.l_of_l):
            raise StopIteration
        item_1 = self.l_of_l[self.index_1]
        item_2 = item_1[self.index_2]
        self.index_2 += 1
        if self.index_2 == len(item_1):
            self.index_2 = 0
            self.index_1 += 1
        return item_2
##for item in FlatIterator(list_of_lists_1):
##    print(item)

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
    



##                           # 2 вариант
##class FlatIterator:
##
##    def __init__(self, list_of_list):
##        self.list_of_list=list_of_list   # список с воложенными списками
##
##    def __iter__(self):
##        self.list_of_list_iter = iter(self.list_of_list)
##        self.nested_list = []  # вложенный список с элементами
##        self.nested_list_cursor = -1
##        return self
##
##    def __next__(self):
##        self.nested_list_cursor += 1
##        if len(self.nested_list) == self.nested_list_cursor:
##            self.nested_list = None
##            self.nested_list_cursor = 0
##            while not self.nested_list:
##                self.nested_list = next(self.list_of_list_iter)
##                #  если  список пустой, то получаем следующий
##                #  если списки закончаться, получим stop iteration
##
##        return self.nested_list[self.nested_list_cursor]                           
##for item in FlatIterator(list_of_lists_1):
##    print(item)
