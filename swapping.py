def main():

    a = input("Enter value for variable 'a': ")

    b = input("Enter value for variable 'b': ")

    print(f"Before swapping: a = {a}, b = {b}")

    temp = a
    a = b
    b = temp

    print(f"After swapping: a = {a}, b = {b}")


if __name__ == "__main__":
    main()
