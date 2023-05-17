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
import json

from pydantic import BaseModel

from .agent_based_api.v1.type_defs import DiscoveryResult
from .agent_based_api.v1 import (
    register,
    Service,
)


DEFAULT_CHECK_LEVELS: Dict = {'river_temperature_levels': (20, 22)}


class Aare(BaseModel):
    location: str
    timestamp: int
    temperature: float
    temperature_prec: float
    temperature_text: str
    temperature_text_short: str
    flow: int
    flow_text: str
    forecast2h: float
    forecast2h_text: str


def parse_aare_guru_aare(string_table) -> Aare:
    if len(string_table) != 1:
        raise ValueError(f'section <<<aare_guru_aare>>> must be a single line but is {len(string_table)} lines')

    raw: dict = json.loads(string_table[0][0])
    return Aare.parse_obj(raw)


register.agent_section(
    name='aare_guru_aare',
    parse_function=parse_aare_guru_aare,
)


def discover_aare_guru_aare(section: Aare) -> DiscoveryResult:
    yield Service()
