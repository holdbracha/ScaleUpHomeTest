from ordered_dict import OrderedDict
import time

def print_action_time_decorator(func):
    def inner(*args, **kwargs):
        start = time.perf_counter_ns()
        res = func(*args, **kwargs)
        end = time.perf_counter_ns()
        print('action took {} ns'.format(end - start))
        return res
    return inner

@print_action_time_decorator
def test_insert(d, k, v):
    if type(d) == type(OrderedDict()):
        d.insert(k, v)
    
    else:
        d[k] = v
        
@print_action_time_decorator
def test_get(d, *args, **kwargs):
    return d.get(*args, **kwargs)

@print_action_time_decorator
def test_keys(d):
    return d.keys()

@print_action_time_decorator
def test_pop(d, k, default = None):
    return d.pop(k, d)

@print_action_time_decorator
def test_update(d, E=None, **F):
    if type(d) == type(OrderedDict()):
        d.update(E, **F)
    
    else:
        if E:
            if type(E) == type(dict()):
                for k in E:
                    d[k] = E[k]

            else:
                for k, v in E:
                    d[k] = v
        
        for k in F:
            d[k] = F[k]

@print_action_time_decorator
def test_pop_first_item(d):
    return d.popfirstitem()

@print_action_time_decorator
def test_clear(d):
    return d.clear()


def main():
    order_dict = OrderedDict()
    regular_dict = {}

    print("********** insert value **********")
    print("Regular dict:")
    test_insert(regular_dict, 5, "hellow")
    print("Order dict:")
    test_insert(order_dict, 5, "hellow")
    print()

    # insert data
    for i in range(5):
        regular_dict[i] = i
        order_dict.insert(i, i)


    print("********** get value **********")
    print("Regular dict:")
    test_get(regular_dict, 5)
    print("Order dict:")
    test_get(order_dict, 5)
    print()

    assert order_dict.get(5) == "hellow", "value of 5 needs to be: hellow"
    assert order_dict.get(6, "world") == "world", "default value of 6 needs to be: world"
    assert order_dict.get(6) == None, "value of 6 needs to be: None"


    print("********** keys **********")
    print("Regular dict:")
    test_keys(regular_dict)
    print("Order dict:")
    test_keys(order_dict)
    print()

    assert order_dict.keys() ==  [5, 0, 1, 2, 3, 4], "keys need to be in order: [5, 0, 1, 2, 3, 4]"


    print("********** pop **********")
    print("Regular dict:")
    test_pop(regular_dict, 2)
    print("Order dict:")
    res = test_pop(order_dict, 2)
    print()

    assert res == 2, "value of key 2 is: 2"
    assert order_dict.keys() ==  [5, 0, 1, 3, 4], "keys need to be in order and without key 2: [5, 0, 1, 3, 4]"
    assert order_dict.pop(8, "not found") ==  "not found", "needs to return default value: not found"


    print("********** update **********")
    print("Regular dict:")
    test_update(regular_dict, {0: "world"})
    print("Order dict:")
    test_update(order_dict, {0: "world"})
    print()

    assert order_dict.get(0) == "world", "value of 0 needs changed to: world"


    print("********** pop first item **********")
    assert test_pop_first_item(order_dict) == "hellow", "value of first key 5 is: hellow"
    assert order_dict.keys() == [0, 1, 3, 4], "keys need to be in order and without first key 5: [0, 1, 3, 4]"
    print()


    print("********** clear **********")
    print("Regular dict:")
    test_clear(regular_dict)
    print("Order dict:")
    test_clear(order_dict)
    print()

    assert order_dict.keys() == [], "there is no keys after clear action"


if __name__ == "__main__":
    main()