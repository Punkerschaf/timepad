from pythonosc import udp_client
from pythonosc.dispatcher import Dispatcher
from pythonosc import osc_server

# convert numpad entry to time-list
def numtl(n):
    lst = list[int]
    match (len(str(n))):
        case 1:
            lst = [0, int(n), 0]
        case 2:
            lst = [0, int(n), 0]
        case 3:
            lst = [0, int(n[0:1]), int(n[1:3])]
        case 4:
            lst = [0, int(n[0:2]), int(n[2:4])]
        case 5:
            lst = [int(n[0:1]), int(n[1:3]), int(n[3:5])]
        case 6:
            lst = [int(n[0:2]), int(n[2:4]), int(n[4:6])]
        case _:
            print('Error in funct no case matches.')
            lst = [0, 0, 0]
    return lst


# converts an integer to string with two characters
def inttostr(tl):
    if len(str(tl)) == 1:
        return "0" + str(tl)
    else:
        return str(tl)


# recalculates times > 60 seconds or minutes
def correctl(tl):
    if type(tl) == list:
        if tl[2] >= 60:
            tl[2] = (tl[2] - 60)
            tl[1] = (tl[1] + 1)
        if tl[1] >= 60:
            tl[1] = (tl[1] - 60)
            tl[0] = (tl[0] + 1)
        return tl
    else:
        print("Error in funct:correcttl: Input is not a list.")
        return tl


# calculate time in seconds. Used for countdown.
def timesecs(tl):
    if type(tl) == list:
        ss = int(tl[2])
        mm = int(tl[1])
        hh = int(tl[0])
        tsec = int(ss + (mm * 60) + (hh * 3600))
        return tsec
    else:
        print("Input for gettimesec is no list.")
        return tl


# build entered time to string with Format HH:mm:ss. Used for countdown to target.
def timestring(tl):
    return str(inttostr(tl[0]) + ":" + inttostr(tl[1]) + ":" + inttostr(tl[2]))


# sending OSC messages to update custom variables in companion.
def updcompanion(tl):
    client.send_message("/custom-variable/timestring/value", timestring(tl))
    client.send_message("/custom-variable/timesecs/value", timesecs(tl))


# called function for OSC numpad entries
def numpadhandler(address: str, *args: list[any]):
    print("Received message with OSC path:" + address + str(args))
    numpad = str(args[0])
    timel = numtl(numpad)
    timel = correctl(timel)
    updcompanion(timel)


### CONFIG ###
# IPs and Ports for OSC configuration
clientip = "127.0.0.1"  # IP of companion
clientport = 12321 # OSC port of companion
serverip = "127.0.0.1" # IP of OSC listener in this script
serverport = 12322 # Port of OSC listener in this script
### /CONFIG ###

if __name__ == '__main__':

# config for UDP sender
    client = udp_client.SimpleUDPClient(clientip, clientport)

# dispatcher for OSC receiver
    dispatcher = Dispatcher()
    dispatcher.map("/timepad/numpad", numpadhandler)

# config and mainloop for OSC listener
    server = osc_server.ThreadingOSCUDPServer(
        (serverip, serverport), dispatcher)
    print("Listening for OSC on {}".format(server.server_address))
    server.serve_forever()
