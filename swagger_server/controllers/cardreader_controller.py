import connexion
import six
import serial

from swagger_server.models.card import Card  # noqa: E501
from swagger_server import util

def cardreader_get_card_number_get():  # noqa: E501
	"""Get cardnumber from serial reader

	Serial connection is initialized for 10 seconds and is awaiting a card to be present # noqa: E501


	:rtype: Card
	"""
	try:
		with serial.Serial('/dev/ttyUSB0', 9600, timeout=10) as ser:
			line = ser.readline()

		if line == "":
			return "Card Not Found", 404
		else:
			return line

	except serial.SerialException:
		return "SerialException: Card Reader Not found", 404