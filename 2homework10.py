import random
from random import randint
import logging
num_ = random.randint(0,50)

for num_ in range(0,50):
	if num_ > 0 and num_ < 9:
		logging.debug(f"The given" {num_} "is in range")
	logging.basicConfig(format="%(asctime)s %(message)s", level=logging.DEBUG)

	if num_ > 10 and num_ < 19:
		logging.info(f"The given" {num_} "is in range. Dont worry.")
	logging.basicConfig(format="%(asctime)s %(message)s", level=logging.info)

	if num_ > 20 and num_ < 29:
		logging.warning(f"The given" {num_} "is raising!")
	logging.basicConfig(format="%(asctime)s %(message)s", level=logging.warning)

	if num_ > 30 and num_ < 39:
		logging.error(f"The given" {num_} "is out of norm!")
	logging.basicConfig(format="%(asctime)s %(message)s", level=logging.error)

	if num_ > 40 and num_ < 50:
		logging.critical(f"The given" {num_} "is not acsepted!")
	logging.basicConfig(format="%(asctime)s %(message)s", level=logging.critical)

	else:
		print("Error!")



