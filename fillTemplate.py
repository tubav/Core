#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Script to generate a scientific paper boiler plate."""

# compatibility for Python 2.x
from __future__ import print_function

__author__ = "Alexander Willner"
__copyright__ = "Copyright 2019, Alexander Willner"
__credits__ = ["Alexander Willner"]
__license__ = "Apache 2.0"
__version__ = "0.0.1"
__maintainer__ = "Alexander Willner"
__email__ = "alex@willner.ws"
__status__ = "Development"

import argparse

CONST_TITLE="What is the core summary of the paper?"
CONST_CONTEXT="What is problem area, why is it interesting?"
CONST_PROBLEM="What is problem we specifically consider, why is it hard? (e.g., why do naive approaches fail?)"
CONST_WORK="Survey past relevant work. Why hasn’t it been solved before? Or, what’s wrong with previous proposed solutions?"
CONST_APPROACH="What are the key components of this approach and how does it differ to related work?"
CONST_EVAL="What are the expected/generated results and how will/have we validate(d) them?"
CONST_RESULT="The expected/generated scientific surplus value?"
CONST_OUTLOOK="How could this work be extended?"

def main(args):
    """ to be done """
    print("First Name: ",args.firstname)
    print("Last Name: ",args.lastname)
    print("Mail: ",args.mail)
    print("Institution: ",args.institution)
    print("Country: ",args.country)
    print("City: ",args.city)
    print("Zip: ",args.zip)
    print("Title: ",args.title)
    print("Context: ",args.context)
    print("Problem: ",args.problem)
    print("Work: ",args.work)
    print("Approach: ",args.approach)
    print("Evaluation: ",args.evaluation)
    print("Result: ",args.result)
    print("Outlook: ",args.outlook)


if __name__ == "__main__":
    PARSER = argparse.ArgumentParser()

    PARSER.add_argument(
        "-v",
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__))

    PARSER.add_argument("-f", "--firstname", action="store", dest="firstname")
    PARSER.add_argument("-l", "--lastname", action="store", dest="lastname")
    PARSER.add_argument("-m", "--mail", action="store", dest="mail")
    PARSER.add_argument("-i", "--institution", action="store", dest="institution")
    PARSER.add_argument("--country", action="store", dest="country")
    PARSER.add_argument("--city", action="store", dest="city")
    PARSER.add_argument("--zip", action="store", dest="zip")
    PARSER.add_argument("-t", "--title", action="store", dest="title", help=CONST_TITLE)
    PARSER.add_argument("-c", "--context", action="store", dest="context", help=CONST_CONTEXT)
    PARSER.add_argument("-p", "--problem", action="store", dest="problem", help=CONST_PROBLEM)
    PARSER.add_argument("-w", "--work", action="store", dest="work", help=CONST_WORK)
    PARSER.add_argument("-a", "--approach", action="store", dest="approach", help=CONST_APPROACH)
    PARSER.add_argument("-r", "--result", action="store", dest="result", help=CONST_RESULT)
    PARSER.add_argument("-e", "--evaluation", action="store", dest="evaluation", help=CONST_EVAL)
    PARSER.add_argument("-o", "--outlook", action="store", dest="outlook", help=CONST_OUTLOOK)	

    MYARGS = PARSER.parse_args()
    main(MYARGS)
