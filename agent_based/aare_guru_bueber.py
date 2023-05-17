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
import json

from pydantic import BaseModel

from .agent_based_api.v1.type_defs import DiscoveryResult, CheckResult
from .agent_based_api.v1 import (
    register,
    Service,
    register,
    Result,
    State,
)


class SwimmingPassage(BaseModel):
    state: str
    state_open_flag: bool


def parse_aare_guru_bueber(string_table) -> SwimmingPassage:
    if len(string_table) != 1:
        raise ValueError(f'section <<<aare_guru_bueber>>> must be a single line but is {len(string_table)} lines')

    raw: dict = json.loads(string_table[0][0])
    return SwimmingPassage.parse_obj(raw)


register.agent_section(
    name='aare_guru_bueber',
    parse_function=parse_aare_guru_bueber,
)


def discover_aare_guru_bueber(section: SwimmingPassage) -> DiscoveryResult:
    yield Service()


def check_aare_guru_bueber(section: SwimmingPassage) -> CheckResult:
    yield Result(state=State.OK, summary='offe' if section.state_open_flag else 'zue')


register.check_plugin(
    name='aare_guru_bueber',
    service_name='Schwümmkanau',
    discovery_function=discover_aare_guru_bueber,
    check_function=check_aare_guru_bueber,
)
