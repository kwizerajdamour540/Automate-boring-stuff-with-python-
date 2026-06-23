import logging

logging.basicConfig(
    filename="debug.log",
    level=logging.DEBUG,
    format="%(levelname)s | %(filename)s | %(funcName)s | %(message)s"
)

def check_divisors():
    print("Checking divisors of 28...")

    for i in range(1, 28):
        if 28 % i == 0:
            logging.debug(f"Divisor found: {i}")

check_divisors()
print("See debug.log")
