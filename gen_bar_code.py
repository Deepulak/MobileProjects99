# pip3 install python-barcode
# import EAN13 from barcode module
from barcode import EAN13
# import ImageWriter to generate an image file
from barcode.writer import ImageWriter

def generator(number):
	# Now let's create an object of EAN13 class and
	# pass the number with the ImageWrite() as the 
	# writer
	my_code = EAN13(number, writer=ImageWriter())
	# Our barcode is ready let's save it 
	my_code.save("bar_code")

if __name__ == "__main__":
	# Make sure to pass the number as string
	generator(input("Enter 12 Digit Number to Generate Bar Code : "))