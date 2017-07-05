#!/usr/bin/env python3

LIGHT_BLUE = '\033[1;34m'
YELLOW = '\033[1;33m'
WHITE = '\033[1;37m'
NO_COLOUR = '\033[0m'


def light_blue(content):
    return coloured(LIGHT_BLUE, content)


def yellow(content):
    return coloured(YELLOW, content)


def white(content):
    return coloured(WHITE, content)


def coloured(colour, content):
    return "{}{}{}".format(colour, content, NO_COLOUR)
