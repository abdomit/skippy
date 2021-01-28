# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 3
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; If not, see <http://www.gnu.org/licenses/>.
#
# ##### END GPL LICENSE BLOCK #####

import PyTango

__author__ = "Benoit Roche"
__maintainer__ = "Benoit Roche"
__email__ = "benoit.roche@esrf.fr"
__copyright__ = "Copyright 2021, ESRF"
__license__ = "GPLv3+"
__status__ = "Test"


Attribute('Voltage_read',
          {'type': PyTango.CmdArgType.DevString,
           'dim': [0],
           'readCmd': "meas:volt?",
           })

Attribute('Voltage',
          {'type': PyTango.CmdArgType.DevDouble,
           'dim': [0],
           'readCmd': "VOLT?",
           'readFormula': "float(VALUE.replace('V', '').strip())",
           'writeCmd': lambda value: "VOLT %s" % (value),
           })

Attribute('Output',
          {'type': PyTango.CmdArgType.DevBoolean,
           'dim': [0],
           'readCmd': "OUTP?",
           'writeCmd': lambda value: "OUTP %s"
           % ('ON' if value else 'OFF'),
           })

Attribute('Remote_Control',
          {'type': PyTango.CmdArgType.DevString,
           'dim': [0],
           'readCmd': "SYST:LOCK:OWN?",
           })

