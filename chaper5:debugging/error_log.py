import logging

logging.basicConfig(
    filename="error.log",
    level=logging.ERROR,
    format="%(levelname)s | %(filename)s | %(funcName)s | %(message)s"
)

def get_number():
    print("Converting input...")

    try:
        int("abc")
    except ValueError:
        logging.error("Input must be an integer")

get_number()
print("See error.log")
