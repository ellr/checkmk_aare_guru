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

from .agent_based_api.v1.type_defs import CheckResult
from .agent_based_api.v1 import (
    register,
    check_levels,
    Result,
    State,
)
from .aare_guru_aare import Aare, discover_aare_guru_aare
from .aare_guru_utils import render_temperature


def check_aare_guru_aare_forecast(section: Aare) -> CheckResult:
    yield from check_levels(
        section.forecast2h,
        metric_name='temperature',
        label='Tämperatur i zwe Stung',
        render_func=render_temperature,
    )
    yield Result(state=State.OK, summary=section.forecast2h_text)


register.check_plugin(
    name='aare_guru_aare_forecast',
    sections=['aare_guru_aare'],
    service_name='Aare: Wasser Tämperatur Vorhärsag',
    discovery_function=discover_aare_guru_aare,
    check_function=check_aare_guru_aare_forecast,
)
