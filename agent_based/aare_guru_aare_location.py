#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-

# This is free software;  you can redistribute it and/or modify it
# under the  terms of the  GNU General Public License  as published by
# the Free Software Foundation in version 2.  check_mk is  distributed
# in the hope that it will be useful, but WITHOUT ANY WARRANTY;  with-
# out even the implied warranty of  MERCHANTABILITY  or  FITNESS FOR A
# PARTICULAR PURPOSE. See the  GNU General Public License for more de-
# tails. You should have  received  a copy of the  GNU  General Public
# License along with GNU Make; see the file  COPYING.  If  not,  write
# to the Free Software Foundation, Inc., 51 Franklin St,  Fifth Floor,
# Boston, MA 02110-1301 USA.

"""
Check_MK agent_based check to use with agent_aare_guru special_agent
This file is written for Check_MK.

Authors:    Roger Ellenberger <roger.ellenberger@wagner.ch>
"""

from __future__ import annotations
from typing import Dict

from .agent_based_api.v1.type_defs import CheckResult
from .agent_based_api.v1 import (
    register,
    Result,
    State,
)
from .aare_guru_aare import Aare, discover_aare_guru_aare


def check_aare_guru_aare_location(section: Aare) -> CheckResult:
    yield Result(state=State.OK, summary=section.location)


register.check_plugin(
    name='aare_guru_aare_location',
    sections=['aare_guru_aare'],
    service_name='Aare: Mäss-Station',
    discovery_function=discover_aare_guru_aare,
    check_function=check_aare_guru_aare_location,
)
