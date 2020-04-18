#!/usr/bin/env python

import os
import sys
sys.path.append(os.environ['PyRes'])  # NL : allow import for modules in PyRes (sonde, stockage, ...)

from mail_faille import *
from suppression_ancienne import *


faille()
deltemps()
