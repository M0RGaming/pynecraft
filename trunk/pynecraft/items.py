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

def load_blocks_and_items():
    for key in BLOCKS_BY_ID.keys():
        BLOCKS_BY_NAME[BLOCKS_BY_ID[key]] = key
    for key in ITEMS_BY_ID.keys():
        ITEMS_BY_NAME[ITEMS_BY_ID[key]] = key
    return

def get_item(item):
    # Is item an ID or name?
    try:
    if type(item) is int or item.isdigit():
        try:
            item = BLOCKS_BY_NAME[BLOCKS_BY_ID[int(item)]]
        except:
            item = ITEMS_BY_NAME[ITEMS_BY_ID[int(item)]]
    else:
        try:
            item = BLOCKS_BY_NAME[item]
        except:
            item = ITEMS_BY_NAME[item]
    except:
        return None
    return item

BLOCKS_BY_ID = {
    0: 'air',
    1: 'stone',
    2: 'grass',
    3: 'dirt',
    4: 'cobblestone',
    5: 'wooden_plank',
    6: 'sapling',
    7: 'bedrock',
    8: 'water',
    9: 'stationary_water',
    10: 'lava',
    11: 'stationary_lava',
    12: 'sand',
    13: 'gravel',
    14: 'gold_ore',
    15: 'iron_ore',
    16: 'coal_ore',
    17: 'wood',
    18: 'leaves',
    19: 'sponge',
    20: 'glass',
    21: 'lapis_lazuli_ore',
    22: 'lapis_lazuli_block',
    23: 'dispenser',
    24: 'sandstone',
    25: 'note_block',
    26: 'bed',
    27: 'powered_rail',
    28: 'detector_rail',
    30: 'web',
    35: 'wool',
    37: 'dandelion',
    38: 'rose',
    39: 'brown_mushroom',
    40: 'red_mushroom',
    41: 'gold_block',
    42: 'iron_block',
    43: 'double_slabs',
    44: 'slabs',
    45: 'block',
    46: 'tnt',
    47: 'bookshelf',
    48: 'moss_stone',
    49: 'obsidian',
    50: 'torch',
    51: 'fire',
    52: 'monster_spawner',
    53: 'wooden_stairs',
    54: 'chest',
    55: 'redstone_wire',
    56: 'diamond_ore',
    57: 'diamond_block',
    58: 'crafting_table',
    59: 'seeds',
    60: 'farmland',
    61: 'furnace',
    62: 'burning_furnace',
    63: 'sign_post',
    64: 'wooden_door',
    65: 'ladders',
    66: 'rails',
    67: 'cobblestone_stairs',
    68: 'wall_sign',
    69: 'lever',
    70: 'stone_pressure_plate',
    71: 'iron_door',
    72: 'wooden_pressure_plate',
    73: 'redstone_ore',
    74: 'glowing_redstone_ore',
    75: 'redstone_torch',
    76: 'redstone_torch_on',
    77: 'stone_button',
    78: 'snow',
    79: 'ice',
    80: 'snow_block',
    81: 'cactus',
    82: 'clay_block',
    83: 'sugar_cane',
    84: 'jukebox',
    85: 'fence',
    86: 'pumpkin',
    87: 'netherrack',
    88: 'soul_sand',
    89: 'glowstone_block',
    90: 'portal',
    91: 'jack-o-lantern',
    92: 'cake_block',
    93: 'redstone_repeater',
    94: 'redstone_repeater_on',
    95: 'locked_chest',
}

# Populated at run time
BLOCKS_BY_NAME = {

}

ITEMS_BY_ID = {
    256: 'iron_shovel',
    257: 'iron_pickaxe',
    258: 'iron_axe',
    259: 'flint_and_steel',
    260: 'apple',
    261: 'bow',
    262: 'arrow',
    263: 'coal',
    264: 'diamond',
    265: 'iron_ingot',
    266: 'gold_ingot',
    267: 'iron_sword',
    268: 'wooden_sword',
    269: 'wooden_shovel',
    270: 'wooden_pickaxe',
    271: 'wooden_axe',
    272: 'stone_sword',
    273: 'stone_shovel',
    274: 'stone_pickaxe',
    275: 'stone_axe',
    276: 'diamond_sword',
    277: 'diamond_shovel',
    278: 'diamond_pickaxe',
    279: 'diamond_axe',
    280: 'stick',
    281: 'bowl',
    282: 'mushroom_soup',
    283: 'gold_sword',
    284: 'gold_shovel',
    285: 'gold_pickaxe',
    286: 'gold_axe',
    287: 'string',
    288: 'feather',
    289: 'gunpowder',
    290: 'wooden_hoe',
    291: 'stone_hoe',
    292: 'iron_hoe',
    293: 'diamond_hoe',
    294: 'gold_hoe',
    295: 'seeds',
    296: 'wheat',
    297: 'bread',
    298: 'leather_cap',
    299: 'leather_tunic',
    300: 'leather_pants',
    301: 'leather_boots',
    302: 'chain_helmet',
    303: 'chain_chestplate',
    304: 'chain_leggings',
    305: 'chain_boots',
    306: 'iron_helmet',
    307: 'iron_chestplate',
    308: 'iron_leggings',
    309: 'iron_boots',
    310: 'diamond_helmet',
    311: 'diamond_chestplate',
    312: 'diamond_leggings',
    313: 'diamond_boots',
    314: 'gold_helmet',
    315: 'gold_chestplate',
    316: 'gold_leggings',
    317: 'gold_boots',
    318: 'flint',
    319: 'raw_porkchop',
    320: 'cooked_porkchop',
    321: 'paintings',
    322: 'golden_apple',
    323: 'sign',
    324: 'wooden_door',
    325: 'bucket',
    326: 'water_bucket',
    327: 'lava_bucket',
    328: 'minecart',
    329: 'saddle',
    330: 'iron_door',
    331: 'redstone',
    332: 'snowball',
    333: 'boat',
    334: 'leather',
    335: 'milk',
    336: 'clay_brick',
    337: 'clay',
    338: 'sugar_cane',
    339: 'paper',
    340: 'book',
    341: 'slimeball',
    342: 'storage_minecart',
    343: 'powered_minecart',
    344: 'egg',
    345: 'compass',
    346: 'fishing_rod',
    347: 'clock',
    348: 'glowstone_dust',
    349: 'raw_fish',
    350: 'cooked_fish',
    351: 'dye',
    352: 'bone',
    353: 'sugar',
    354: 'cake',
    355: 'bed',
    356: 'redstone_repeater',
    357: 'cookie',
    2256: 'gold_music_disc',
    2257: 'green_music_disc',
}

# Populated at run time
ITEMS_BY_NAME = {}
