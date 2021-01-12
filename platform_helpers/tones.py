# Tone generation functions.
#
# Copyright (C) 2021, Ty Gillespie. All rights reserved.
# MIT License.

import ctypes
import platform

# Windows DLL handle.
if platform.system() == "Windows":
 kernel32 = ctypes.windll.kernel32

class UnsupportedPlatformError(Exception):
 """Raised when a platform isn't currently supported."""
 pass

def beep(frequency, length):
 """Beeps a tone."""
 if platform.system() == "Windows":
  kernel32.Beep(frequency, length)
  return True
 else:
  raise UnsupportedPlatformError("Beeping is not currently supported with this module on this platform.")
  return False
