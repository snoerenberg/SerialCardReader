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
		with serial.Serial('/dev/ttyUSB0', 9600, timeout=10) as ser:	# open serial port with 10 seconds timeout
			serialInput = ser.readline().strip()						# readline and trim whitespaces/newline
	
	except serial.SerialException:
		return "SerialException: Card Reader Not found", 404
	
	else:
		if not serialInput:												# serial input was empty
			return "Card Not Found", 404
		
		else:
			try:
				cardNumber = int(serialInput)							# parse to int to make sure its numeric and leading zeros cut off
				return cardNumber
			except ValueError:
				return "Cardnumber was not numeric", 404

