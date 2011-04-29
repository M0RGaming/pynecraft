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

class TestMinecraftServer(MinecraftServer):

    def __init__(self):
        self.msgs = []
        return

    def start(self):
        """ Override """
        return

    def stdin(self, msg):
        """ Override """
        self.msgs.append(msg)
        return

    def get_stdin(self):
        return msgs

    def clear(self):
        self.msgs = []
        return

class TestOutput:

    def __init__(self):
        return

class CommandsTest:

    def setUp(self):
        self.server = TestMinecraftServer()
        return

    def test_help_command(self):
        output = {}
        help_command(self.server, output, conf)
        self.assertEquals(self.server.get_stdin())
        return

    def test_give_command(self.):
        return

    def test_kit_command(self):
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

    def test_demod_command():
        return
