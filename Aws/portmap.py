#! /usr/bin/python3

from socket import *
import os
import sys
import getopt
import time

# Create the log file
path = "portmap_logs/"
if not os.path.exists(path):
    os.makedirs(path)
fileName = "portmap_logs/" + time.strftime("%d-%m-%Y") \
        + "@" + time.strftime("%H:%M:%S")+".log"
logFile = open(fileName, "w+")


# Try to open a socket connected to the given port and host.
# There's probably a more elegant solution but this one works.
def checkPort(hostname, port, timeout=2):
    try:
        sock = socket(family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None)
        sock.settimeout(timeout)
        portOpen = sock.connect((hostname, port))
        sock.close()
        logFile.write(str(port)+"\n")
        print(port, "Open")
    except:
        print(port, "Closed")


# Print a list of command line arguments.
def printArgs():
    print("Short |    Long    |  Arguments | Explanation\n"
          "  -h  |   --help   |   <none>   | Display this help text\n"
          "  -u  |   --host   | <hostname> | Supply a hostname to probe\n"
          "  -p  |   --port   |   <port>   | Specify a single port to test\n"
          "  -s  |--rangestart|<start port>| Specify the staring port\n"
          "  -e  | --rangeend | <end port> | Specify the ending port\n"
          "  -t  | --timeout  | <timeout>  | \
                  Specify a timeout in seconds per test")


# Parse command line arguments and check the relevant ports.
def main(argv):
    # Useful variables
    port = 0
    rangeStart = 0
    rangeEnd = 0
    timeout = 2
    host = ""
    if len(argv) <= 0:
        printArgs()
        sys.exit(-1)
    try:
        opts, args = getopt.getopt(argv, "hu:p:s:e:t:",
                                   [
                                       "help=",
                                       "host=",
                                       "port=",
                                       "rangestart=",
                                       "rangeend=",
                                       "timeout="
                                   ])
    except getopt.GetoptError:
        printArgs()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            printArgs()
            sys.exit()
        elif opt in ("-u", "--host"):
            host = arg
        elif opt in ("-p", "--port"):
            port = int(arg)
        elif opt in ("-s", "--rangestart"):
            rangeStart = int(arg)
        elif opt in ("-e", "--rangeend"):
            rangeEnd = int(arg)
        elif opt in ("-t", "--timeout"):
            timeout = float(arg)
    logFile.write("--" + host + "--\n")
    if port != 0:
        checkPort(host, port, timeout)
    else:
        for cPort in range(rangeStart, rangeEnd + 1):
            checkPort(host, cPort, timeout)
# Start the main function with command line arguments
if __name__ == "__main__":
    main(sys.argv[1:])
