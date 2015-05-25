#!/usr/bin/env python
import argparse
import sys


class Domain(object):
    def __init__(self, domain):
        """Constructor"""
        if sys.version_info[0] < 3:
            domain = domain.decode('utf-8').encode('utf-8')
            idna = domain.decode('utf-8').encode('idna')
            self.ascii = idna
            self.utf_8 = idna.decode('idna').encode('utf-8')
        else:
            idna = bytes(domain, 'idna')
            self.ascii = idna.decode('ascii')
            self.utf_8 = idna.decode('idna')
        if self.ascii == self.utf_8:
            self.type = 'ascii'
            self.utf_8 = None
        else:
            if self.utf_8 == domain:
                self.type = 'unicode'
            else:
                self.type = 'punycode'

    def display(self):
        print('INPUT: \x1B[1m{}\x1B[0m\nASCII: \x1B[1m{}\x1B[0m'
              .format(self.type, self.ascii))
        if self.utf_8 is not None:
            print('UTF-8: \x1B[1m{}\x1B[0m'.format(self.utf_8))

def parse_arguments(sysargs):
    """Parse and store arguments."""
    desc = 'A simple punycode to unicode and back converter.'
    p = argparse.ArgumentParser(description=desc)

    p.add_argument('domain', help='domain name to convert')

    # Store the supplied args
    return p.parse_args(sysargs)


def main(main_sysargs):
    args = parse_arguments(main_sysargs[1:])

    domain = Domain(args.domain)
    domain.display()


if __name__ == '__main__':
    main(sys.argv)

