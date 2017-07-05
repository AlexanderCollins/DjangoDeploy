#!/usr/bin/env python3
from modules.colours import *
from modules.asset_paths import ASSETS


def get_banner():
    # load ascii banner
    with open(ASSETS.get("banner"), 'r') as f:
        ascii_banner = f.readlines()
        f.close()
    return light_blue("".join(ascii_banner))


def get_website():
    # load website url
    with open(ASSETS.get("website"), 'r') as f:
        website_url = f.readlines()
        f.close()
    return yellow("".join(website_url))


def get_github():
    # load github url
    with open(ASSETS.get("github"), 'r') as f:
        github_url = f.readlines()
        f.close()
    return yellow("".join(github_url))


def get_version():
    # load version number
    with open(ASSETS.get("version"), 'r') as f:
        version = f.readlines()
        f.close()
    return white("".join(version))


def get_welcome():
    # load welcome message
    with open(ASSETS.get("welcome"), 'r') as f:
        welcome_message = f.readlines()
        f.close()
    return white("".join(welcome_message))


def get_confirmation():
    # load confirmation message
    with open(ASSETS.get("confirmation"), 'r') as f:
        confirmation_message = f.readlines()
        f.close()
    return white("".join(confirmation_message))
