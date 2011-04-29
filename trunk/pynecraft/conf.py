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

### Configuration ###

COMMANDS = {
    '!help': 'help_command',
    '!ban': 'ban_command',
    '!kick': 'kick_command',
#    '!backup': 'backup_command',
    '!mods': 'mods_command',
    '!mod': 'mod_command',
    '!demod': 'demod_command',
    '!give': 'give_command',
    '!kit': 'kit_command',
    '!kits': 'kits_command',
}

PLUGINS = ()

COMMAND = ('java',
           '-Xms1024M',
           '-Xmx1024M',
           '-jar',
           'minecraft_server.jar',
           'nogui')

RESTART_TIME = 5 # seconds

CONFIG = {
    'ops_file': 'ops.txt',
    'mods_file': 'mods.txt',
    'log_file': 'pynecraft.log',
    'kits_file': 'kits.ini',
    'server_properties_file': 'server.properties',
    'backup_command': {
        'script': 'python backup_maps.py',
        'directory': 'backup'
    },
}
