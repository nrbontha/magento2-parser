#!/usr/bin/env python3

import re

def dedupe_pattern(string, pattern):
    if pattern*2 in string:
        return dedupe_pattern(string.replace(pattern*2, pattern), pattern)
    return string

def replace_pattern(string, pattern, replace):
    output = re.sub(pattern, replace, string)
    if replace*2 in output:    
        output = dedupe_pattern(output, replace)
    return output
