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

from pynecraft.items import *

import unittest

class ItemsTest(unittest.TestCase):

    def setUp(self):
        return

    def test_load_blocks_and_items(self):
        # Make sure all the blocks and
        # items are loaded correctly
        load_blocks_and_items()
        for key in BLOCKS_BY_ID.keys():
            self.assertTrue(BLOCKS_BY_ID[key] in BLOCKS_BY_NAME.keys())
            self.assertEquals(key, BLOCKS_BY_NAME[BLOCKS_BY_ID[key]])
        for key in ITEMS_BY_ID.keys():
            self.assertTrue(ITEMS_BY_ID[key] in ITEMS_BY_NAME.keys())
            self.assertEquals(key, ITEMS_BY_NAME[ITEMS_BY_ID[key]])
        return

    def test_get_item(self):
        # Load by ID
        self.assertEquals(10, get_item(10))
        # Load by name
        self.assertEquals(10, get_item('lava'))
        # Load non-existent item
        self.assertEquals(None, get_item('herpderp'))
        return

if __name__ == '__main__':
    unittest.main()
