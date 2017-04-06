"""Cricket Score.

Usage: 
    notification.py -time T
    notification.py -h --help

T : time between notifications in seconds
  
Options:
  -h --help     Show this screen.
  --version     Show version.

"""

from gi.repository import Notify
import json
import cricbuzz
import time
from docopt import docopt

while True:
    arguments = docopt(__doc__, version='1.0')
    cricbuzz.get_cricket_scores()

    with open('data.json') as data_file:
        cricket_matches = json.load(data_file)

    message = '\n'
    for series in cricket_matches:
        message += cricket_matches[series]["Batting team"] + ': '
        message += cricket_matches[series]["Batting Team Runs"] + '/'
        message += cricket_matches[series]["Batting Team Wickets"] + ' (Overs : '
        message += cricket_matches[series]["Batting Team Overs"] + ')\n'
        try:
            message += cricket_matches[series]["Bowling team"] + ': '
            message += cricket_matches[series]["Bowling Team Runs"] + '/'
            message += cricket_matches[series]["Bowling Team Wickets"] + ' (Overs : '
            message += cricket_matches[series]["Bowling Team Overs"] + ')\n'
        except TypeError:
            message += "Did not bat"
        message += '-------------------------------------------------\n'
    notifier = Notify.init("warning")
    notifier = Notify.Notification.new(message)
    notifier.set_urgency(2)
    notifier.show()
    time.sleep(10)
    notifier.close()
    time.sleep(int(arguments['T']) - 10)
