#!/usr/bin/env python3
from argparse import ArgumentParser
from random import randint
from sys import argv
from time import sleep, strftime
import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify

URGENCY = 0
TITLE = 'EYE WATCH'
MESSAGES = (
    'do some blinking',
    'roll your eyes a few times',
    'look at a distant object',
    'close your eyes tightly for a few seconds',
    'move your eyes sideways'
)


def parse_args():
    desc = 'display a reminder to take a short break and do some eye practice'
    parser = ArgumentParser(description=desc)
    parser.add_argument(
        '-t',
        '--timer',
        default='600',
        help=('run in foreground, showing notification every TIMER seconds '
              '(this is default, with TIMER = 600)')
    )
    parser.add_argument(
        '-i',
        '--icon',
        help='show ICON alongside the message'
    )
    return parser.parse_args()


def get_random_message(message_list):
    list_len = len(message_list)
    random_value = randint(0, list_len - 1)
    return message_list[random_value]


def show_notification(notification, text=None, icon=None):
    notification.update(TITLE, text, icon)
    notification.set_urgency(URGENCY)
    notification.show()


def main():
    args = parse_args()
    Notify.init(argv[0])
    notification = Notify.Notification.new(summary=TITLE)

    show_notification(notification, 'Eyewatch daemon started!', args.icon)
    while True:
        sleep(int(args.timer))
        text = get_random_message(MESSAGES)
        show_notification(notification, text, args.icon)

    Notify.uninit()

if __name__ == '__main__':
    main()
