#
#  --------------------------------------------------------------------------
#   Mildtrix Ltd
#
#
#
#  Filename: $HeadURL$
#
#  Version: $Revision$,
#                   $Date$
#                   $Author$
#
#  Copyright (c) Mildtrix Ltd
#
# ---------------------------------------------------------------------------
#
#   DESCRIPTION
#
#  This file is a part of Mildtrix Device Framework.
#
#  Mildtrix Device Framework is Open Source software; you can redistribute it
#  and/or modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; version 2 of the License.
#  Mildtrix Device Framework is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#  See the GNU General Public License for more details.
#
#  More information of Mildtrix products: http://www.mildtrix.org
#
#  This code is licensed under the GNU General Public License v2.
#  Full text may be retrieved at http://www.gnu.org/licenses/gpl-2.0.txt
# ---------------------------------------------------------------------------
from .MILDObisValueItem import MILDObisValueItem

class MILDObisValueItemCollection(list):
   #
    # Constructor.
    #
    # forParent: Parent object.
    #
    def __init__(self, forParent=None):
        list.__init__(self)
        # Parent object.
        self.parent = forParent

    def append(self, item):
        if not isinstance(item, MILDObisValueItem):
            raise TypeError('item is not of type MILDObisValueItem')
        if not self.contains(item):
            super(MILDObisValueItemCollection, self).append(item)

    def contains(self, item):
        for it in self:
            if it.value == item.value:
                return True
        return False
