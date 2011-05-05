"""
Copyright (c) 2011 Derek Schaefer

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

from pynecraft.server import MinecraftServer
from pynecraft.commands import *
from pynecraft.kits import load_kits

import os
import unittest

KITS_EXPECTED = ['give other_player 310 1\n', 'give other_player 311 1\n', 'give other_player 312 1\n', 'give other_player 313 1\n']

class TestLog:

    def into(self, msg): return
    def error(self, msg): return

class TestMinecraftServer(MinecraftServer):

    def __init__(self, mods):
        self.mods = mods # Override the mods property
        self.msgs = []
        MinecraftServer.__init__(self, os.getcwd(), TestLog())
        return

    def start(self):
        """ Override """
        return

    def stdin(self, msg):
        """ Override """
        self.msgs.append(msg)
        return

    def get_stdin(self):
        return self.msgs

    def clear(self):
        self.msgs = []
        return

class TestOutput:

    def __init__(self, d):
        for key,value in d.items():
            setattr(self, key, value)
        return

class CommandsTest(unittest.TestCase):

    def setUp(self):
        self.name = 'derp'
        self.mods = [self.name]
        self.server = TestMinecraftServer(mods=self.mods)
        return

    def test_help_command(self):
        output = TestOutput({
            'name': self.name,
            'command': '!help',
            'message': '',
            'args': []
        })
        help_command(self.server, output, None)
        self.assertEquals(list, type(self.server.get_stdin()))
        self.assertEquals(1 + len(COMMANDS), len(self.server.get_stdin()))
        return

    def test_give_command(self):
        load_blocks_and_items() # Load item names
        msg = 'other_player tnt 10'
        output = TestOutput({
            'name': self.name,
            'command': '!give',
            'message': msg,
            'args': msg.split()
        })
        give_command(self.server, output, None)
        self.assertEquals(['give other_player 46 10\n'], self.server.get_stdin())
        return

    def test_kit_command(self):
        load_kits(self.server)
        msg = 'other_player armor'
        output = TestOutput({
            'name': self.name,
            'command': '!kit',
            'message': msg,
            'args': msg.split()
        })
        kit_command(self.server, output, None)
        self.assertEquals(KITS_EXPECTED, self.server.get_stdin())
        return

    def test_kits_command(self):
        return

    def test_ban_command(self):
        return

    def test_kick_command(self):
        return

    def test_backup_command(self):
        return

    def test_mods_command(self):
        return

    def test_mod_command(self):
        return

    def test_demod_command(self):
        return
