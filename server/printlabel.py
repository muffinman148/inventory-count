### Import Python Modules
import MySQLdb
import datetime
import socket
import sys
import re

### Database Configuration
# TODO Make file for reference to private info
config = {
    'user': '',
    'passwd': '',
    'host': '',
    'db': 'dbInv',
}

### Printer Configuration
printer_ip = '10.93.0.33'
printer_port = 9100

partNum = "SP0328"

### Database Connections
cnx = MySQLdb.connect(**config)
cursor = cnx.cursor()
cursor_unbuf = cnx.cursor()

# TODO Remove hardcode and replace with variable
query = ("SELECT ProductLine, ItemCode, SalesUnitOfMeasure, ItemCodeDesc, PrimaryVendorNo FROM rpi_inv_ci_item WHERE ItemCode = 'SP0328';")
cursor.execute(query)


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = (printer_ip, printer_port)
sock.connect(server_address)

# The following codes are compatible with a Brother QL-720NW

NUL                  = chr(0x00)                                                                               
EOT                  = chr(0x04)                                                                               
HT                   = chr(0x09) # horizontal tab                                                             
LF                   = chr(0x0a)                                                                               
FF                   = chr(0x0c) # Form feed (Print)                                                          
DLE                  = chr(0x10)                                                                               
ESC                  = chr(0x1b) # Escape                                                                     
FS                   = chr(0x1c)                                                                               
GS                   = chr(0x1d)                                                                               
CRLF                 = chr(0x0d) + chr(0x0a) # Carriage return / Line feed                                    
BOLDON               = chr(0x1b) + chr(0x45) # Bold On                                                        
BOLDOFF              = chr(0x1b) + chr(0x46) # Bold Off                                                       
FONT_BROUGHAM        = chr(0x1b) + chr(0x6b) + chr(0x00) # Set font to Brougham (Bitmap fixed)                
FONT_LETTERGOTHIC    = chr(0x1b) + chr(0x6b) + chr(0x01) # Set font to Letter Gothic (Bitmap fixed)           
FONT_BRUSSELS        = chr(0x1b) + chr(0x6b) + chr(0x02) # Set font to Brussels (Bitmap Proportional)         
FONT_HELSINKI        = chr(0x1b) + chr(0x6b) + chr(0x03) # Set font to Helsinki (Bitmap Proportional)         
FONT_SANDIEGO        = chr(0x1b) + chr(0x6b) + chr(0x04) # Set font to San Diego (Bitmap Proportional)        
FONT_LETTERGOTHIC_OL = chr(0x1b) + chr(0x6b) + chr(0x09) # Set font to Letter Gothic (Outline fixed)          
FONT_BRUSSELS_OL     = chr(0x1b) + chr(0x6b) + chr(0x0a) # Set font to Brussels (Outline Proportional)        
FONT_HELSINKI_OL     = chr(0x1b) + chr(0x6b) + chr(0x0b) # Set font to Helsinki (Outline Proportional)        
LANDSCAPE            = chr(0x1b) + chr(0x69) + chr(0x4c) + chr(0x01) # Set to Landscape                       
ESPCMODE             = chr(0x1b) + chr(0x61) + chr(0x69) + chr(0x00) # Select ESC/P mode                      
INIT                 = chr(0x1b) + chr(0x40) # Initalize                                                      
FONTSIZE             = chr(0x1b) + chr(0x58) + chr(0x00) # Set font size  nL nH                               
MINLF                = chr(0x1b) + chr(0x33) # Specify minimum line feed n (0-255)                            
BACKSLASH            = chr(0x5c)                                                                               

# Builds Barcode
BARCODE = ESC + chr(0x69) + chr(0x74) + chr(0x30) + chr(0x72) + chr(0x30) + chr(0x68) + chr(0x68) + chr(0x00) + chr(0x77) + chr(0x31) + chr(0x7A) + chr(0x32) + chr(0x42)

# Creates Label
def createESCpLabel(result):
    code = str(ItemCode)
    string = ESPCMODE + INIT + LANDSCAPE + FONT_HELSINKI_OL
    string += FONTSIZE + chr(58) + NUL
    string += ProductLine + " " + BOLDON + ItemCode + BOLDOFF + " "
    string += ESC + chr(0x24) + chr(0x20) + chr(0x03) + SalesUnitOfMeasure + CRLF
    string += BARCODE + code + BACKSLASH + CRLF
    string += cleanString(ItemCodeDesc) + CRLF
    string += PrimaryVendorNo + CRLF
    string += FF
    return string.encode()

# UTF-8 Compatible Print
def cleanString(s):
    print(s)

    d = {
        '⅛' : '1/8',
        '¼' : '1/4',
        '⅜' : '3/8',
        "½" : '1/2',
        '⅝' : '5/8',
        '¾' : '3/4',
        '⅞' : '7/8'
    }
    pattern = re.compile(r'\b(' + '|'.join(d.keys()) + r')\b')
    result = pattern.sub(lambda x: d[x.group()], s)
    return result
    
    
for (ProductLine, ItemCode, SalesUnitOfMeasure, ItemCodeDesc, PrimaryVendorNo) in cursor:
    try:
        labeldata = createESCpLabel(cursor)
        sock.sendall(labeldata)

    finally:
        sock.close()
