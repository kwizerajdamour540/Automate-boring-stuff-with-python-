import logging

logging.basicConfig(
    filename="info.log",
    level=logging.INFO,
    format="%(levelname)s | %(filename)s | %(funcName)s | %(message)s"
)

def check_perfect_number():
    print("Checking perfect number...")

    num = 28
    logging.info(f"{num} is being checked")

check_perfect_number()
print("See info.log")
