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
from dlms_mt.MILDIntEnum import MILDIntEnum

class TokenDelivery(MILDIntEnum):
    """
    Enumerates token delivery methods.
    Online help:
    http://www.mildtrix.fi/Mildtrix.DLMS.Objects.MILDDLMSTokenGateway
    """
    #pylint: disable=too-few-public-methods

    #
    # Via remote communications.
    #
    REMOTE = 0
    #
    # Via local communications.
    #
    LOCAL = 1
    #
    # Via manual entry.
    #
    MANUAL = 2
