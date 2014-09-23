# -*- coding: utf-8 -*-
# Copyright (C) 2013-2014 Fox Wilson, Peter Foley, Srijay Kasturi,
# Samuel Damashek, James Forcier, and Reed Koser
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301,
# USA.

import re
from requests import get
from html.parser import HTMLParser
from random import random, choice, randrange


def removevowels(msg):
    return re.sub('[aeiouy]', '', msg, flags=re.I)


def gen_word():
    html = get('http://randomword.setgetgo.com/get.php').text
    # Strip BOM
    return html[3:].rstrip()


def gen_fwilson(x, mode=None):
    if x.lower().startswith('fwil'):
        mode = 'w'
    if mode is None:
        mode = 'w' if random() < 0.5 else 'f'
    if mode == 'w':
        output = "wh%s %s" % ('e' * randrange(3, 20), x)
        return output.upper()
    else:
        output = ['fwil%s' % q for q in x.split()]
        output = ' '.join(output)
        return output.lower()


def gen_creffett(msg):
    return '\x02\x038,4%s!!!' % msg.upper()


def gen_slogan(msg):
    html = get('http://www.sloganizer.net/en/outbound.php', params={'slogan': msg})
    slogan = re.search('>(.*)<', html.text).group(1)
    parser = HTMLParser()
    slogan = parser.unescape(parser.unescape(slogan))
    slogan = slogan.replace('\\', '').strip()
    return slogan if slogan else gen_slogan(msg)


def gen_morse(msg):
    morse_codes = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.",
                   "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..",
                   "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.",
                   "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
                   "y": "-.--", "z": "--..", "1": ".----", "2": "..---", "3": "...--",
                   "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..",
                   "9": "----.", "0": "-----", " ": "  ", ".": ".-.-.-", ",": "--..--",
                   "?": "..--..", "'": ".----.", "!": "-.-.--", "/": "-..-.", "(": "-.--.",
                   ")": "-.--.-", "&": ".-...", ":": "---...", ";": "-.-.-.", "=": "-...-",
                   "+": ".-.-.", "-": "-....-", "_": "..--.-", '"': ".-..-.", "$": "...-..-", "@": ".--.-."}
    morse = ""
    for i in msg:
        try:
            morse += morse_codes[i.lower()] + " "
        except Exception:
            morse += "? "
    return morse


def gen_insult(user):
    adj = [
        "acidic", "antique", "contemptible", "culturally-unsound",
        "despicable", "evil", "fermented", "festering", "foul", "fulminating",
        "humid", "impure", "inept", "inferior", "industrial", "left-over",
        "low-quality", "malodorous", "off-color", "penguin-molesting",
        "petrified", "pointy-nosed", "salty", "sausage-snorfling", "tastless",
        "tempestuous", "tepid", "tofu-nibbling", "unintelligent", "unoriginal",
        "uninspiring", "weasel-smelling", "wretched", "spam-sucking",
        "egg-sucking", "decayed", "halfbaked", "infected", "squishy", "porous",
        "pickled", "coughed-up", "thick", "vapid", "hacked-up", "unmuzzleld",
        "bawdy", "vain", "lumpish", "churlish", "fobbing", "rank", "craven",
        "puking", "jarring", "fly-bitten", "pox-marked", "fen-sucked",
        "spongy", "droning", "gleeking", "warped", "currish", "milk-livered",
        "surly", "mammering", "ill-borne", "beef-witted", "tickle-brained",
        "half-faced", "headless", "wayward", "rump-fed", "onion-eyed",
        "beslubbering", "villainous", "lewd-minded", "cockered", "full-gorged",
        "rude-snouted", "crook-pated", "pribbling", "dread-bolted",
        "fool-born", "puny", "fawning", "sheep-biting", "dankish", "goatish",
        "weather-bitten", "knotty-pated", "malt-wormy", "saucyspleened",
        "motley-mind", "it-fowling", "vassal-willed", "loggerheaded",
        "clapper-clawed", "frothy", "ruttish", "clouted", "common-kissing",
        "pignutted", "folly-fallen", "plume-plucked", "flap-mouthed",
        "swag-bellied", "dizzy-eyed", "gorbellied", "weedy", "reeky",
        "measled", "spur-galled", "mangled", "impertinent", "bootless",
        "toad-spotted", "hasty-witted", "horn-beat", "yeasty", "boil-brained",
        "tottering", "hedge-born", "hugger-muggered", "elf-skinned"]
    amt = [
        "accumulation", "bucket", "coagulation", "enema-bucketful", "gob",
        "half-mouthful", "heap", "mass", "mound", "petrification", "pile",
        "puddle", "stack", "thimbleful", "tongueful", "ooze", "quart", "bag",
        "plate", "ass-full", "assload"]
    noun = [
        "bat toenails", "bug spit", "cat hair", "chicken piss", "dog vomit",
        "dung", "fat-woman's stomach-bile", "fish heads", "guano", "gunk",
        "pond scum", "rat retch", "red dye number-9", "Sun IPC manuals",
        "waffle-house grits", "yoo-hoo", "dog balls", "seagull puke",
        "cat bladders", "pus", "urine samples", "squirrel guts",
        "snake assholes", "snake bait", "buzzard gizzards", "cat-hair-balls",
        "rat-farts", "pods", "armadillo snouts", "entrails", "snake snot",
        "eel ooze", "slurpee-backwash", "toxic waste", "Stimpy-drool", "poopy",
        "poop", "craptacular carpet droppings", "jizzum", "cold sores",
        "anal warts"]
    msg = '%s is a %s %s of %s.' % (user, choice(adj), choice(amt), choice(noun))
    return msg


def char_to_bin(c):
    i = ord(c)
    n = 8
    # We need to be able to handle wchars
    if i > 1 << 8:
        n = 16
    if i > 1 << 16:
        n = 32
    ret = ""
    for j in range(n):
        ret += str(i & 1)
        i >>= 1
    return ret[::-1]


def gen_binary(string):
    return "".join(map(char_to_bin, string))


def gen_clippy(nick, msg):
    return '%s: I see you are trying to %s, would you like some help with that?' % (nick, msg)


def do_xkcd_sub(msg, hook=False):
    # http://xkcd.com/1288/
    substitutions = {'witnesses': 'these dudes I know',
                     'allegedly': 'kinda probably', 'new study': 'tumblr post',
                     'rebuild': 'avenge', 'space': 'SPAAAAAACCCEEEEE',
                     'google glass': 'virtual boy', 'smartphone': 'pokedex',
                     'electric': 'atomic', 'senator': 'elf-lord', 'car': 'cat',
                     'election': 'eating contest', 'congressional leaders':
                     'river spirits', 'homeland security': 'homestar runner',
                     'could not be reached for comment':
                     'is guilty and everyone knows it'}
    # http://xkcd.com/1031/
    substitutions['keyboard'] = 'leopard'
    # http://xkcd.com/1418/
    substitutions['force'] = 'horse'
    output = msg
    # for creffett
    if not hook or ('space' in output and random() < 0.3) or random() < 0.25:
        for text, replacement in substitutions.items():
            if text in output:
                output = re.sub(r"\b%s\b" % text, replacement, output)

    output = re.sub(r'(.*)(?:-ass )(.*)', r'\1 ass-\2', output)
    if msg == output:
        return None if hook else msg
    else:
        return output
