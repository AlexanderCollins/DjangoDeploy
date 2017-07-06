#!/usr/bin/env python3
from modules.colours import *
from modules.asset_paths import ASSETS


def fetch_assets(asset_name):
    with open(ASSETS.get(asset_name), 'r') as f:
        content = f.readlines()
        f.close()
        return content


def get_banner():
    # load ascii banner
    ascii_banner = fetch_assets('banner')
    return light_blue("".join(ascii_banner))


def get_website():
    # load website url
    website_url = fetch_assets('website')
    return yellow("".join(website_url))


def get_github():
    # load github url
    github_url = fetch_assets('github')
    return yellow("".join(github_url))


def get_version():
    # load version number
    version = fetch_assets('version')
    return white("".join(version))


def get_welcome():
    # load welcome message
    welcome_message = fetch_assets('welcome')
    return white("".join(welcome_message))


def get_confirmation():
    # load confirmation message
    confirmation_message = fetch_assets('confirmation')
    return white("".join(confirmation_message))

