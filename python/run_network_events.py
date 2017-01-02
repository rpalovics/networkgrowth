import sys
from stats.network_events import NetworkEvents

file_name = sys.argv[1]
out_file = sys.argv[2]

events = NetworkEvents(file_name,out_file)
events.run()
