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

def parse_args(sys_args):
    desc = 'display a reminder to take a short break and do some eye practice'
    p = ArgumentParser(description=desc)
    p.add_argument(
        '-t',
        '--timer',
        default='600',
        help='run in foreground, showing notification every TIMER seconds (this is default, with TIMER = 300)'
    )
    p.add_argument(
        '-o',
        '--once',
        action='store_true',
        default=False,
        help='show notification once and exit'
    )
    p.add_argument(
        '-i',
        '--icon',
        help='show ICON alongside the message'
    )
    return p.parse_args(sys_args)

def get_random_message(message_list):
    list_len = len(message_list)
    random_value = randint(0, list_len - 1)
    return message_list[random_value]

def show_notification(notification, icon):
    text = get_random_message(MESSAGES)
    print('[' + strftime('%H:%M:%S') + '] ' + text)
    if icon is not None:
        notification.update(TITLE, text, icon)
    else:
        notification.update(TITLE, text)
    notification.set_urgency(URGENCY)
    notification.show()

if __name__ == '__main__':
    args = parse_args(argv[1:])
    Notify.init(argv[0])
    notification = Notify.Notification.new(summary=TITLE)

    if args.once == True:
        show_notification(notification, args.icon)
    else:
        while True:
            sleep(int(args.timer))
            show_notification(notification, args.icon)

    Notify.uninit()
