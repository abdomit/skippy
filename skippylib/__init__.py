# -*- coding: utf-8 -*-
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

# from .abstracts import (AbstractSkippyObj, AbstractSkippyAttribute,
#                         AbstractSkippyFeature)
from .attributes import (SkippyAttribute, SkippyReadAttribute,
                         SkippyReadWriteAttribute)
from .builder import Builder, AttrExc
from .communications import CommunicatorBuilder
from .features import (SkippyFeature, RampFeature, RawDataFeature,
                       ArrayDataInterpreterFeature)
from .skippy import Skippy
from .version import version
from .watchdog import WatchDog


__author__ = "Sergi Blanch-Torné"
__email__ = "sblanch@cells.es"
__copyright__ = "Copyright 2017, CELLS / ALBA Synchrotron"
__license__ = "GPLv3+"
