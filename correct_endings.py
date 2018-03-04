#! /usr/bin/python3
# -*- coding: utf-8 -*-
import argparse
import re
from os.path import join
from glob import glob

LIST_OF_WORDS = ["a", "i", "o", "u", "w", "z", "ze", "od", "do", "że", "iż",
                 "poprzez", "przez", "spod", "sponad", "znad", "po", "za", "nad", "pod", "na",
                 "oraz", "ale", "lub", "albo", "bądź", "czy", "by", "aby", "jak", "ponieważ", "bo",
                 "który", "która", "które", "którego", "któremu", "której", "którym",
                 "to", "te", "są", "się", "dla", "jest", "być", "lecz", "wraz", "nie", "tak",
                 "więc", "niech", "tylko"]

LIST_OF_WORDS += [word + "," for word in LIST_OF_WORDS]
LIST_OF_WORDS += [word.title() for word in LIST_OF_WORDS]


def add_hard_spaces(path_to_tex_files):
    files = glob(join(path_to_tex_files, "*.tex"))
    if not files:
        exit("No .tex files found")

    for file in files:
        print("fixing: " + file)
        with open(file, encoding="utf-8") as f:
            lines = f.readlines()
        with open(file, encoding="utf-8", mode="w") as out:
            for line in lines:
                out.write(fix_line(line))


def fix_line(line):
    if line.startswith("\\") or line.startswith("%"):
        return line
    for word in LIST_OF_WORDS:
        line = re.sub(" {} ".format(word), " {}~".format(word), line)
        line = re.sub("^{} ".format(word), "{}~".format(word), line)
    return line


def cofigure_args_and_help():
    parser = argparse.ArgumentParser(description="This script adds hard spaces (~) to your .tex files.")
    parser.add_argument("PATH", type=str, nargs="?", default=".", help="Path to directory with your .tex files")
    return parser.parse_args()


if __name__ == "__main__":
    args = cofigure_args_and_help()
    add_hard_spaces(args.PATH)
