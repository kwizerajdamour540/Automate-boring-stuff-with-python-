import logging

logging.basicConfig(
    filename="warning.log",
    level=logging.WARNING,
    format="%(levelname)s | %(filename)s | %(funcName)s | %(message)s"
)

def check_odd_number():
    print("Checking number...")

    num = 21

    if num % 2 != 0:
        logging.warning("Perfect numbers are usually even")

check_odd_number()
print("See warning.log")
