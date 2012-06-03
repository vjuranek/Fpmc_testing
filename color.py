#!/usr/bin/env python

#Ulitility for color output

NONE         = ""
BLACK        = "\033[0;30m"
RED          = "\033[0;31m"
GREEN        = "\033[0;32m"
BROWN        = "\033[0;33m"
BLUE         = "\033[0;34m"
PURPLE       = "\033[0;35m"
CYAN         = "\033[0;36m"
LIGHT_GREY   = "\033[0;37m"
DARK_GREY    = "\033[1;30m"
LIGHT_RED    = "\033[1;31m"
LIGHT_GREEN  = "\033[1;32m"
YELLOW       = "\033[1;33m"
LIGHT_BLUE   = "\033[1;34m"
LIGHT_PURPLE = "\033[1;35m"
LIGHT_CYAN   = "\033[1;36m"
WHITE        = "\033[1;37m"
DEFAULT      = "\033[0m"

COLOREND     = "\033[1;m"

def printColor(text,col):
    print col + text + COLOREND

def red(text):
    return LIGHT_RED + text + COLOREND

def green(text):
    return LIGHT_GREEN + text + COLOREND

def yellow(text):
    return YELLOW + text + COLOREND

def blue(text):
    return LIGHT_BLUE + text + COLOREND
