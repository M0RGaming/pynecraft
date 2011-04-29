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

import os
import time
import logging

LOG_LEVEL = logging.DEBUG
LOG_FMT = '%(asctime)s [%(levelname)s] %(message)s'

def init_logging(cwd):
    """ Sets up the logging system """
    logger = logging.getLogger()
    logger.setLevel(LOG_LEVEL)
    # Create file handler
    fh = logging.FileHandler(os.path.join(cwd, CONFIG['log_file']))
    fh.setLevel(LOG_LEVEL)
    # Create console handler
    ch = logging.StreamHandler()
    ch.setLevel(LOG_LEVEL)
    # Create formatter and add it to the handlers
    formatter = logging.Formatter(LOG_FMT)
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)
    # Add the handlers to logger
    logger.addHandler(ch)
    logger.addHandler(fh)
    return logger

def attach_commands():
    """ Attaches command functions to COMMANDS in conf """
    import pynecraft.commands
    remove = []
    for cmd in COMMANDS:
        try:
            COMMANDS[cmd] = pynecraft.commands.__dict__[COMMANDS[cmd]]
        except Exception, e:
            # Remove the command if the function
            # cannot be found
            remove.append(cmd)
            print 'Unable to load command %s: %s' % (cmd, str(e))
    for r in remove:
        del COMMANDS[cmd]
    return

def start_plugins(server):
    """ Initializes all plugins """
    plugins = []
    for plugin in PLUGINS:
        if plugin.__name__ in CONFIG:
            plugins.append(plugin(server, Config[CONFIG[plugin.__name__]]))
        else:
            plugins.append(plugin(server, None))
        plugins[-1].start()
    return plugins

def stop_plugins(plugins):
    """ Stops all plugins """
    for p in plugins:
        p.stop = True
    time.sleep(RESTART_TIME)
    return

def run_command(command, server, output):
    """ Runs a command """
    if not command in COMMANDS: return
    if command in CONFIG:
        COMMANDS[command](server, output, Config(CONFIG[command]))
    else:
        COMMANDS[command](server, output, None)
    return

def parse_properties(server):
    """ Parses the Minecraft properties file """
    properties = {}
    f = open(os.path.join(server.cwd, CONFIG['server_properties_file']), 'r')
    for line in f:
        line = line.strip()
        if not line.startswith("#"):
            (key, sep, val) = line.partition("=")
            properties[key] = val
    return properties
