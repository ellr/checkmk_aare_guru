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

from .agent_based_api.v1.type_defs import CheckResult, DiscoveryResult
from .agent_based_api.v1 import (
    register,
    Service,
    Result,
    State,
)
from .aare_guru_weather import (
    check_aare_guru_weather_temp,
    check_aare_guru_weather_rain,
)


def discover_aare_guru_weather_current(section_aare_guru_weather, section_aare_guru_sun) -> DiscoveryResult:
    yield Service()


def check_aare_guru_weather_current(section_aare_guru_weather, section_aare_guru_sun) -> CheckResult:
    weather = section_aare_guru_weather.current
    sun = section_aare_guru_sun.today

    yield from check_aare_guru_weather_temp(
        temperature=weather.air_temperature,
    )
    yield from check_aare_guru_weather_rain(
        rainfall=weather.rainfall,
    )
    yield Result(state=State.OK, summary=f'Sunnestunge: {sun.suntotal}')


register.check_plugin(
    name='aare_guru_weather_current',
    sections=['aare_guru_weather', 'aare_guru_sun'],
    service_name='Wätter: jtze grad',
    discovery_function=discover_aare_guru_weather_current,
    check_function=check_aare_guru_weather_current,
)
