"""
Demonstrates how to read the device name string from a LabJack.

"""

from labjack import ljm


# Open first found LabJack
handle = ljm.open(ljm.constants.dtANY, ljm.constants.ctANY, "LJM_idANY")[2]
#handle = ljm.openS("LJM_dtANY", "LJM_ctANY", "LJM_idANY")

info = ljm.getHandleInfo(handle)
print "Opened a LabJack with Device type: %i, Connection type: %i,\n" \
    "Serial number: %i, IP address: %s, Port: %i,\nMax bytes per MB: %i" % \
    (info[0], info[1], info[2], ljm.numberToIP(info[3]), info[4], info[5])

# Call eReadString to read the name string from the LabJack.
string = ljm.eReadString(handle, "DEVICE_NAME")

print "\nDevice name : %s" % string

# Close handle
ljm.close(handle)