#!/usr/bin/env python3

import re

EMAIL = re.compile(r"^.{1,1023}@[a-zA-Z{1} a-zA-Z|0-9][. a-zA-Z{1}a-zA-Z|0-9]*.{1,253}$")