from linked_list import *
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
def test_append(l, val):
    l.append(val)
   
@print_action_time_decorator
def test_get_node(l, val):
    if type(l) == type(Node()):
        return get_node(l, val)
    return l.index(val)

def main():
    my_list = Node()
    regular_list = [1]

    print("********** append value **********")
    print("Regular list:")
    test_append(regular_list, 2)
    print("Linked list:")
    test_append(my_list, 2)
    print()

    print("********** get node **********")
    print("Regular list:")
    test_get_node(regular_list, 2)
    print("Linked list:")
    test_get_node(my_list, 2)

    # insert data
    for i in range(5):
        my_list.append(i)

    temp_list = Node(50)
    assert check_circular_list(my_list) == False, "the list has no circul"
    assert check_lists_merging(my_list, temp_list) == False, "2 differents lists"
    temp_list.nextval = my_list.nextval
    assert check_lists_merging(my_list, temp_list) == True, "margin lists"
    my_list.link_end_to_first()
    assert check_circular_list(my_list) == True, "the list has a circul"

if __name__ == "__main__":
    main()