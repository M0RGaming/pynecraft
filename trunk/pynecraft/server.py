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

from pynecraft.conf import *
from pynecraft.items import *
from pynecraft.kits import *
from pynecraft.util import *

import os
import sys
import time
import fnmatch
import subprocess

def run(cwd):
    """ Top level function for running the server """
    # Configure logging
    log = init_logging(cwd)

    # Start the server
    try:
        server = MinecraftServer(cwd, log)
        log.info('Starting server...')
        server.start()
    except Exception, e:
        # Something went south when starting
        # the server, so let's exit
        log.error(str(e))
        sys.exit()

    # Main Pynecraft loop
    while True:
        try:
            output_str = server.stderr
            if not output_str: continue
            if 'INFO' in output_str:
                output = Output(output_str)
                if output.command in COMMANDS:
                    try:
                        run_command(output.command, server, output)
                    except Exception, e:
                        log.error(str(e))
                        server.tell(output.name, 'Command failed: %s' % str(e))
                elif output.command[0] == '!':
                    msg = 'Unknown command "%s"' % output.command
                    server.tell(output.name, msg)
        except KeyboardInterrupt:
            # Ctrl-C signal was caught
            log.info('Stopping the server...')
            server.shutdown()
            sys.exit()
        except IOError, e:
            # The server process closed or is
            # no longer producing or accepting input
            log.error(str(e))
            sys.exit()
        except Exception, e:
            # Exception was probably Python-based
            # so keep going
            log.error(str(e))

    return

###
### Begin: Server classes
###

class MinecraftServer:
    """ Interfaces with the Minecraft server """

    def __init__(self, cwd, log):
        self.cwd = cwd
        self.log = log
        self.kits = []
        return

    @property
    def kits(self):
        """ Returns all Kit objects """
        return self.kits

    def kit(self, output, target, kit):
        """ Gives the kit to a player """
        for k in self.kits:
            if k.name == kit:
                for item in k.items:
                    self.give(target.lower(), item['item'], item['qty'])
                return
        self.tell(output.name, 'Unknown kit "%s"' % kit)
        return

    def op(self, name):
        """ Ops the player """
        self.stdin('op %s\n' % (name))
        return

    def deop(self, name):
        """ Deops the player """
        self.stdin('deop %s\n' % (name))
        return

    def mod(self, output, name):
        """ Mods the player """
        mods_file = os.path.join(self.cwd, CONFIG['mods_file'])
        mode = 'a' if os.path.exists(mods_file) else 'w'
        mods_file = open(mods_file, mode)
        mods_file.write('%s\n' % (name))
        mods_file.flush()
        mods_file.close()
        self.tell(output.name, '%s is now a mod' % name)
        return

    def demod(self, output, name):
        """ Demods the player """
        mods = self.mods
        mods_file = os.path.join(self.cwd, CONFIG['mods_file'])
        mode_file = open(mods_file, 'w+')
        for mod in mods:
            if mod != name.lower():
                mods_file.write(mod)
                mods_file.flush()
        mods_file.close()
        self.tell(output.name, '%s is no longer a mod' % name)
        return

    def give(self, name, item, num=1):
        """ Gives the item to a player """
        self.stdin('give %s %s %s\n' % (name, item, num))
        return

    def kick(self, name):
        """ Kicks the player from the server """
        self.stdin('kick %s\n' % (name))
        return

    def ban(self, name):
        """ Bans the player from the server """
        self.stdin('ban %s\n' % (name))
        return

    def banip(self, ip):
        """ Bans the IP from the server """
        self.stdin('banip %s\n' % (ip))
        return

    def unban(self, name):
        """ Removes the player from the ban list """
        self.stdin('unban %s\n' % (name))
        return

    def say(self, msg):
        """ Sends the message to all players """
        self.stdin('say %s\n' % (msg))
        return

    def tell(self, name, msg):
        """ Sends a message to a single player """
        self.stdin('tell %s %s\n' % (name, msg))
        return

    def start(self):
        """ Starts the server and initializes all modules """
        time.sleep(RESTART_TIME)
        self.process = subprocess.Popen(COMMAND,
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE,
                                        stdin=subprocess.PIPE)
        # Wait for the server to start up
        time.sleep(5) # Usually only takes like long, could bump it up
        self.properties = parse_properties(self)
        self.plugins = start_plugins(self)
        load_blocks_and_items()
        load_kits(self)
        attach_commands()
        self.log.info('Finished starting up')
        return

    def shutdown(self):
        """ Shuts down the server and all modules """
        self.plugins = stop_plugins(self.plugins)
        self.stdin('stop\n')
        return

    def save_stop(self):
        """ Stops saving chunks """
        self.stdin('save-stop\n')
        return

    def save_start(self):
        """ Starts saving chunks """
        self.stdin('save-start\n')
        return

    def save_all(self):
        """ Forces the server to save changes """
        self.stdin('save-all\n')
        return

    def list(self):
        """ Returns a list of all players on the server """
#        self.stdin('list')
#        out = self.stderr.split()
        return
        

    def stdin(self, msg):
        """ Writes to the stdin of the server process """
        self.process.stdin.write(msg)
        self.process.stdin.flush()
        return

    @property
    def stdout(self):
        """ Reads the stdout of the server process """
        return self.process.stdout.readline().strip()

    @property
    def stderr(self):
        """ Reads the stderr of the server process """
        return self.process.stderr.readline().strip()

    @property
    def ops(self):
        """ Returns the list of server ops """
        ops_file = os.path.join(self.cwd, CONFIG['ops_file'])
        mode = 'r' if os.path.exists(ops_file) else 'w+'
        ops_file = open(ops_file, mode)
        ops = []
        for o in ops_file.read().splitlines():
            if o: ops.append(o)
        ops_file.close()
        return ops

    @property
    def mods(self):
        """ Returns the list of server mods """
        mods_file = os.path.join(self.cwd, CONFIG['mods_file'])
        mode = 'r' if os.path.exists(mods_file) else 'w+'
        mods_file = open(mods_file, mode)
        mods = []
        for m in mods_file.read().splitlines():
            if m: mods.append(m)
        mods_file.close()
        return mods

    @property
    def players(self):
        """ Returns the list of players registered on the server """
        world = self.properties['level-name']
        try:
            files = os.listdir(os.path.join(self.cwd, world, 'players'))
            players = []
            for f in files:
                if fnmatch.fnmatch(f, '*.dat'):
                    players.append(f[:-4].lower())
            return players
        except:
            pass
        return []

class Output:
    """ Parses and stores output from the Minecraft server """

    def __init__(self, output):
        self.output = output.split()
        self.DATE_INDEX = 0
        self.TIME_INDEX = 1
        self.PLAYER_INDEX = 3
        self.COMMAND_INDEX = 4
        self.COMMAND_ARGS_INDEX = 5
        return

    @property
    def time(self):
        return '%s %s' % (self.output[self.DATE_INDEX], self.output[self.TIME_INDEX])

    @property
    def name(self):
        return self.output[self.PLAYER_INDEX][1:-1].lower()

    @property
    def command(self):
        return self.output[self.COMMAND_INDEX]

    @property
    def message(self):
        return ' '.join(self.output[self.COMMAND_INDEX:])

    @property
    def args(self):
        try:
            return self.output[self.COMMAND_ARGS_INDEX:]
        except:
            pass
        return []

class Config:
    """ Parses and stores the Pynecraft CONFIG """

    def __init__(self, conf):
        for key, value in conf.items():
            setattr(self, key, value)
        return
