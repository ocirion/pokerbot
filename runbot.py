import argparse
import socket
import sys
from Player import Player

parser = argparse.ArgumentParser(description='A Pokerbot.', add_help=False, prog='pokerbot')
parser.add_argument('-h', dest='host', type=str, default='localhost', help='Host to connect to, defaults to localhost')
parser.add_argument('port', metavar='PORT', type=int, help='Port on host to connect to')
args = parser.parse_args()

# Create a socket connection to the engine.
print 'Connecting to %s:%d' % (args.host, args.port)
try:
    s = socket.create_connection((args.host, args.port))
except socket.error as e:
    print 'Error connecting! Aborting'
    exit()

bot = Player()
bot.run(s)
