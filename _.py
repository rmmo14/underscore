class Underscore:
    def map(self, iterable, callback):
        # your code here
        for i in range(0, len(iterable)):
            iterable[i] = callback(iterable[i])
        print(iterable)
        return iterable
    def find(self, iterable, callback):
        # your code here
        for i in range(0, len(iterable)):
            if callback(iterable[i]):
                print(iterable[i])
                break
        return iterable[i]
    def filter(self, iterable, callback):
        # your code
        arr2 = []
        for i in range(0, len(iterable)):
            if callback(iterable[i]):
                arr2.append(iterable[i])
        print(arr2)
        return arr2
    def reject(self, iterable, callback):
        # your code
        arr = []
        arr2 = []
        for i in range(0, len(iterable)):
            if callback(iterable[i]):
                arr.append(iterable[i])
            else:
                arr2.append(iterable[i])
        print(arr2)
        return arr2
# you just created a library with 4 methods!
# let's create an instance of our class
_ = Underscore() # yes we are setting our instance to a variable that is an underscore
# evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
# should return [2, 4, 6] after you finish implementing the code above
_.map([1,2,3], lambda x: x*2) # should return [2,4,6]
_.find([1,2,3,4,5,6], lambda x: x>4) # should return the first value that is greater than 4
_.filter([1,2,3,4,5,6], lambda x: x%2==0) # should return [2,4,6]
_.reject([1,2,3,4,5,6], lambda x: x%2==0) # should return [1,3,5]