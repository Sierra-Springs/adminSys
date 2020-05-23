#!/usr/bin/env python

import os
import sys
sys.path.append(os.environ['PyRes'])  # NL : allow import for modules in PyRes (sonde, stockage, ...)
sys.path.append(os.environ['Stockage'])

from fctmail import *
from faille import *
from suppression_ancienne import *
from graphique import *

faille()
#deltemps()
