# Tone generation functions.
#
# Copyright (C) 2020-2021, Ty Gillespie. All rights reserved.
# MIT License.

import ctypes
import platform
from exceptions import *

system = platform.system()

# Windows DLL handle.
if platform.system() == "Windows":
 kernel32 = ctypes.windll.kernel32

def beep(frequency, length):
 """Beeps a tone."""
 if system == "Windows":
  kernel32.Beep(frequency, length)
  return True
 else:
  raise UnsupportedPlatformError("Beeping is not currently supported with this module on " + system + ".")
  return False
