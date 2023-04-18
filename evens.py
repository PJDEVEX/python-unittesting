def even_number_of_evens(numbers):
    """
    Test to be performed:
    Should Raise a TypeError if a list in not passed into the function
    error message: "A list was not passed into the function"
    if the list is empty it will return False
    if the number of even numbers is odd - return False
    if the numner of even numbers is even - return True
    """
    if isinstance(numbers, list):
        if numbers == []:
            return False
    else:
        raise TypeError("A list not passed into the fuction")


if __name__ == '__main__':
    print(even_number_of_evens(5))
