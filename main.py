# Ken Holm
# Purpose: Demonstrate how to handle errors (es) nicely
#  See https://docs.python.org/3/library/es.html
#  for e types

# Jump into an infinite loop, for testing
while True:

    # Try to run some code
    try:
        firstInteger = int(input("Please enter an integer: "))
        secondInteger = int(input("Please enter another integer: "))
        print(f"{firstInteger} divided by {secondInteger} is {firstInteger / secondInteger}")

    # Nicely fail on an OS error
    #  See https://docs.python.org/3/library/es.html#OSError
    except OSError as e:
        print(f"It appears an OS e was raised")
        print(f"\t{e}")

    # Nicely fail if we have a value error
    #  See https://docs.python.org/3/library/es.html#ValueError
    except ValueError as e:
        print(f"It appears that input is not an integer")
        print(f"\t{e}")

    # Nicely fail when trying to divide by zero
    #  See https://docs.python.org/3/library/es.html#ZeroDivisionError
    except ZeroDivisionError as e:
        print(f"It appears that your second integer is zero.")
        print(f"\t{e}")

    # Nicely fail for everything else (i.e., unknown errors)
    except Exception as e:
        print(f"Something else went wrong")
        print(f"\t{e}")

    # Final clean up
    finally:
        print(f" FINALLY ".center(20, "="))
        print()
