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

from pynecraft.conf import CONFIG
from pynecraft.items import get_item

import os
import ConfigParser

class Kit:
    def __init__(self, name, items):
        self.name = name
        self.items = items
        return

def load_kits(server):
    kits = ConfigParser.ConfigParser()
    kits.read(os.path.join(server.cwd, CONFIG['kits_file']))
    for kit in kits.sections():
        items = []
        for item in kits.items(kit):
            # Make sure the items exist
            try:
                i = get_item(item[0])
                if i is None:
                    print 'Invalid item "%s", skipping...' % item[0]
                    continue
                else:
                    items.append({'item':i, 'qty':int(item[1])})
            except:
                print 'Invalid quantity "%s", skipping item...' % item[1]
                continue
        if len(items) > 0:
            server.kits_list.append(Kit(kit, items))
        else:
            print 'Invalid kit "%s", skipping...' % kit
    return
