from qrtools import QR
my_QR = QR(filename = "home/user/Desktop/qr.png")
  
# decodes the QR code and returns True if successful
my_QR.decode()
  
# prints the data
print (my_QR.data)
