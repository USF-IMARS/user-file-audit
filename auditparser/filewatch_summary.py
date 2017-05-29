#!/usr/bin/env python

# import argparse
import sys
import select

def summarize_ausearch_string(the_str):
    """
    creates summary of given string from `ausearch -i` (or similar)
    """
    cursor = 0
    summary_dict = {}
    # === possilby useful substrings:
    #    user:
    #       auid=7yl4r uid=7yl4r euid=7yl4r suid=7yl4r fsuid=7yl4r
    #    group:
    #       gid=common egid=common sgid=common fsgid=common
    substr = " uid="
    while (True):
        cursor = the_str.find(substr, cursor+1)  # move to next location of substr
        # print(cursor)

        if (cursor < 0): # if no next location
            break
        else:
            key_start = cursor + len(substr)
            key_end = the_str.index(" ", cursor+1)
            # print(key_start, ':', key_end)
            key = the_str[key_start:key_end]
            try:
                summary_dict[key] += 1
            except KeyError:
                summary_dict[key] = 1
    return summary_dict

if __name__ == "__main__":
    # parser = argparse.ArgumentParser(description='summarize ausearch filewatch results')
    #
    # # parser.add_argument("-v", "--verbose", help="increase output verbosity",
    # #                     action="count",
    # #                     default=0
    # # )
    #
    # parser.add_argument("logstring", help="string text from `ausearch -i` to parse")
    # args = parser.parse_args()
    # logstring = args.logstring
    if not sys.stdin.isatty():
        logstring = ''.join([l for l in sys.stdin.readlines()])
        print(summarize_ausearch_string(logstring))
    else:
        print("no data")
