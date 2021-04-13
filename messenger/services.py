#!/usr/bin/env python3
# -*-encoding: utf-8-*-

import re


def valid_mail(mail: str) -> bool:
    """
    validation mail name
    using regex
    """

    success = False

    pattern = re.compile(r'[\w.]+@([\w-]+\.)+[\w-]{2,4}')
    matched = pattern.match(mail)  # None if isn't matched
    if matched is not None:
        # if matched
        # checking matched length
        success = matched.start() == 0 and matched.end() == len(mail)
    return success


def valid_message(msg: str) -> bool:
    """
    validation msg text
    must not be empty
    length < 100
    """
    return bool(msg.replace(' ', '')) and len(msg) < 100
