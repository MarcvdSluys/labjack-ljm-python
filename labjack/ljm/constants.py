"""
LJM library constants.

"""

# Read/Write direction constants:
READ = 0
WRITE = 1

# Data types:
# Automatic endian conversion, if needed by the processor
UINT16 = 0
UINT32 = 1
INT32 = 2
FLOAT32 = 3

# Advanced users data type:
# Does not do any endianness conversion
BYTE = 99
STRING = 98
STRING_MAX_SIZE = 49
STRING_ALLOCATION_SIZE = 50

# namesToAddresses sets this when a register name is not found
INVALID_NAME_ADDRESS = -1
MAX_NAME_SIZE = 256

MAC_STRING_SIZE = 18
IPv4_STRING_SIZE = 16

NOT_ENOUGH_DATA_SPACE = 9999.99

# Device types:
dtANY = 0
dtUE9 = 9
dtU3 = 3
dtU6 = 6
dtT7 = 7
dtSKYMOTE_BRIDGE = 1000
dtDIGIT = 200

# Connection types:
ctANY = 0
ctUSB = 1
ctTCP = 2
ctETHERNET = 3
ctWIFI = 4

# TCP/Ethernet constants:
NO_IP_ADDRESS = 0
NO_PORT = 0
DEFAULT_PORT = 502

# Identifier types:
DEMO_MODE = "-1"
idANY = 0

# addressesToMBFB Constants
DEFAULT_FEEDBACK_ALLOCATION_SIZE = 62
USE_DEFAULT_MAXBYTESPERMBFB = 0

# listAll Constants
LIST_ALL_SIZE = 128

MAX_USB_PACKET_NUM_BYTES = 64
MAX_TCP_PACKET_NUM_BYTES_T7 = 1400
MAX_TCP_PACKETS_NUM_BYTES_NON_T7 = 64

# Timeout Constants
NO_TIMEOUT = 0
DEFAULT_TIMEOUT = 1000

# Config Parameters
SEND_RECEIVE_TIMEOUT_MS = "LJM_SEND_RECEIVE_TIMEOUT_MS"
OPEN_TCP_DEVICE_TIMEOUT_MS = "LJM_OPEN_TCP_DEVICE_TIMEOUT_MS"
LOG_MODE = "LJM_LOG_MODE"
LOG_LEVEL = "LJM_LOG_LEVEL"
LIBRARY_VERSION = "LJM_LIBRARY_VERSION"
ALLOWS_AUTO_MULTIPLE_FEEDBACKS = "LJM_ALLOWS_AUTO_MULTIPLE_FEEDBACKS"
OPEN_MODE = "LJM_OPEN_MODE";
NAME_CONSTANTS_FILE = "LJM_NAME_CONSTANTS_FILE"
ERROR_CONSTANTS_FILE = "LJM_ERROR_CONSTANTS_FILE"
LOG_FILE = "LJM_LOG_FILE"
CONSTANTS_FILE = "LJM_CONSTANTS_FILE"

# Config Values

# LJM_LOG_LEVEL:
# WARNING: These may change, and some may disappear
TRACE = 2
DEBUG = 4
INFO = 6
PACKET = 7
WARNING = 8
ERROR = 10
FATAL = 12

# LJM_OPEN_MODE
KEEP_OPEN = 1
OPEN_CLOSE = 2
