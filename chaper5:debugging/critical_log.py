import logging

logging.basicConfig(
    filename="critical.log",
    level=logging.CRITICAL,
    format="%(levelname)s | %(filename)s | %(funcName)s | %(message)s"
)

def validate_number():
    print("Validating number...")

    num = -28

    if num < 0:
        logging.critical("Negative numbers are not allowed")

validate_number()
print("See critical.log")
