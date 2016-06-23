#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding=utf-8
#
# Welcome to 🔑++, the programming language they don't want you to use.
# For more information about language functionality, check out
# https://github.com/rrshaban/keyplusplus
#
#

from __future__ import print_function

import sys
import ast
import re

# These are the regular expressions that define the language. As of now,
# they include multi-line regexes, which might require hacking newlines.
k = {
    "boilerplate"   :   r"^#DJKHALED\n#WETHEBEST",
    "import"        :   r"fanluv (?P<libname>\w+?)\b",
    "def"           :   r"they don't want you to (?P<func_name>\w*?) (?P<args>[\w ]*)\n (?P<body>.*?)🙏",
    "="             :   r"🔑 (?P<left>\w*) (?P<right>.*)",
    "loops"         :   r"ride wit me(?P<loop>.*?)another one",
    "break"         :   r"you played yourself",
    "return"        :   r"major 🔑 (?P<return>\w*?)",
    "print"         :   r"🔥 (?P<print>.+)",
    "true"          :   r"(?P<true>👍)",
    "false"         :   r"(?P<false>👎)",
    "struct"        :   r"(?P<struct>\w*?) talk(?P<fields>.*)you smart",
    "fields"        :   r"(🔑 [\w_]*$)+",
    "function"      :   r"(?P<function>\w+) vibes (?P<args>[\w ]*)\n",
}

def replace(p):
    # Python for 🔑++
    # TODO: structs and fields remain to be implemented

    subs = [
        (k["true"],     r"True"),
        (k["false"],    r"False"),
        (k["import"],   r"import \g<libname>"),
        (k["return"],   r"return \g<return>"),
        (k["="],        r"\g<left> = \g<right>"),
        (k["function"], r"\g<function>(\g<args>)"),
        (k["print"],    r"print(\g<print>)"),
        (k["break"],    r"break"),
    ]

    for pattern, replacement in subs:
        p = re.sub(pattern, replacement, p)

    p = re.sub(k["loops"],  r"while True:\n \g<loop>", p, 
            flags=re.DOTALL)
    p = re.sub(k["def"],    r"def \g<func_name>(\g<args>):\n \g<body>", p, 
            flags=re.DOTALL)
    
    return p

def parse_v2(program):

    # check for boilerplate
    if not re.match(k["boilerplate"], program):
        raise SyntaxError("You played yourself. #DJKHALED #WETHEBEST")

    return ast.parse(replace(program))

def main():

    if len(sys.argv) < 2:
        raise IOError('''
            Congratulations, you played yourself. You must pass the 🔑++ a file to run:

            e.g. 🔑++ hello.liooooon
            ''')

    try: 
        f = open(sys.argv[1], 'r')
        program = f.read()
        exec(compile(parse_v2(program), filename="<🔑++>", mode="exec")) 
    except IOError:
        print("Could not open {}. You played yourself.".format(sys.argv[1]))

if __name__ == '__main__':
  main()

