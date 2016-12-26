# simulate for loop with iterator
def my_for_loop(some_iter):
    # create a __iter__() object from the some_iter input
    obj_iter = some_iter.__iter__()
    # continuously print the .next() element if the __iter__() object
    while True:
        try:
            print obj_iter.next()
        # until it raises StopIteration exception at the end of the __iter__() object
        except StopIteration:
            # break out the while seeing the exception at the end
            break

my_for_loop([1, 2, 3])
