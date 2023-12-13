import types
                            # 1 вариант
##list_of_lists_2 = [
##        [['a'], ['b', 'c']],
##        ['d', 'e', [['f'], 'h'], False],
##        [1, 2, None, [[[[['!']]]]], []]
##    ]



def flat_generator(list_of_lists_2):
    for item in list_of_lists_2:
        if isinstance(item, list):
            # если элемент списка оказывается списком то оборачиваем в этот же генратор
            # такой прием называется рекурсия
            for sub_item in flat_generator(item):
                yield sub_item
        else:
            yield item
##for item in flat_generator(list_of_lists_2):
##    print(item)


def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_4()
