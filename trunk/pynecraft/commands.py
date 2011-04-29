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
from pynecraft.decorators import *
from pynecraft.items import *

### Command functions ###

@is_mod
def help_command(server, output, conf):
    """ Prints the list of commands """
    server.tell(output.name, 'Available commands:')
    for key in COMMANDS.keys():
        cmd_func = COMMANDS[key]
        if cmd_func.__doc__:
            server.tell(output.name, '%s: %s' % (key[1:], cmd_func.__doc__))
        else:
            server.tell(output.name, key[1:])
    return

@is_mod
def give_command(server, output, conf):
    """ Give an item to a player """
    args = output.args
    if len(args) == 2:
        # Default quantity
        target = args[0]
        item = args[1]
        qty = 1
    elif len(args) == 3:
        # Custom quantity
        target = args[0]
        item = args[1]
        qty = args[2]
    else:
        server.tell(output.name, 'Incorrect arguments')
        return

    item_id = get_item(item)
    if item_id is None:
        server.tell(output.name, 'Unknown item "%s"' % item)
    else:
        server.give(target, item_id, qty)

    return

@is_mod
def kit_command(server, output, conf):
    """ Gives a kit of items to a player """
    args = output.args
    if len(args) == 2:
        target = args[0].lower()
        kit = args[1].lower()
    else:
        server.tell(output.name, 'Incorrect arguments')
        return

    server.kit(output, target, kit)

    return

@is_mod
def kits_command(server, output, conf):
    """ Lists all available kits """
    for kit in server.kits:
        server.tell(output.name, kit.name)
    return

@is_op
def ban_command(server, output, conf):
    """ Bans a player from the server """
    for target in output.message.split()[1:]:
        if target in server.ops:
            server.tell(output.name, 'Operators cannot be banned')
            continue
        server.banip(target)
        server.ban(target)
    return

@is_op
def kick_command(server, output, conf):
    """ Kicks a player from the server """
    for target in output.message.split()[1:]:
        if target in server.ops:
            server.tell(output.name, 'Operators cannot be kicked')
            continue
        server.kick(target)
    return

@is_op
def backup_command(server, output, conf):
    """ Backs up the server """
    subprocess.call(CONFIG['backup_command']['script'].split())
    return

@is_mod
def mods_command(server, output, conf):
    """ Lists all server moderators """
    mods = server.mods
    if len(mods) > 0:
        server.tell(output.name, 'Moderators:')
        for mod in mods:
            server.tell(output.name, mod)
    else:
        server.tell(output.name, 'There are no moderators')
    return

@is_op
def mod_command(server, output, conf):
    """ Adds the player to the mod list """
    for target in output.message.split()[1:]:
        if target in server.ops:
            server.tell(output.name, '%s is an operator' % (target))
            continue
        if target in server.mods:
            server.tell(output.name, '%s is already a mod' % (target))
        else:
            server.mod(output, target)
    return

@is_op
def demod_command(server, output, conf):
    """ Remove the player from the mod list """
    for target in output.message.split()[1:]:
        if target in server.ops:
            server.tell(output.name, '%s is an operator' % (target))
            continue
        if not target in server.mods:
            server.tell(output.name, '%s is not a mod' % (target))
        else:
            server.demod(output, target)
    return
