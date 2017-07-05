#!/usr/bin/env python3
from modules import asset_paths as assets
import unittest
import os.path


class TestAssetPathsMethods(unittest.TestCase):

    def test_exists_asset_paths(self):
        try:
            assets.ASSETS
        except NameError as error:
            self.fail(error)

    def test_files_exits_asset_paths(self):
        for key in assets.ASSETS:
            if not os.path.exists(assets.ASSETS[key]):
                self.fail(
                    FileNotFoundError("Could not find asset.\nkey: {}, path: {}.".format(key, assets.ASSETS[key]))
                )
