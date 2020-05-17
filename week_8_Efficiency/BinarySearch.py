# full output of binary search without comments
import random

numbers = [random.randint(0, 30) for i in range(10)]


def binarySearch(List, num):
    List.sort()

    while List:

        mid = len(List) // 2  # divides the list

        if List[mid] == num:
            return True

        elif List[mid] > num:

            List = List[: mid]

        elif List[mid] < num:
            List = List[mid + 1:]

    return False


print(sorted(numbers))
print(binarySearch(numbers, 20))
