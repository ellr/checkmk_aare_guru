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

from .aare_guru_utils import render_temperature

from .agent_based_api.v1.type_defs import CheckResult
from .agent_based_api.v1 import (
    register,
    Service,
    Result,
    State,
)
from .aare_guru_weather import (
    Weather,
    WeatherForecast,
    check_aare_guru_weather_rain,
)


def discover_aare_guru_weather_forecast(section: Weather):
    for i, _ in enumerate(section.forecast):
        yield Service(item=f'{i+1}')


def check_aare_guru_weather_forecast(item: str, section: Weather) -> CheckResult:
    i = int(item) - 1
    weather: WeatherForecast = section.forecast[i]

    yield Result(state=State.OK, summary=f'Vorhersag füre {weather.day}: {weather.weather_text}')
    yield Result(
        state=State.OK,
        summary=(f'Luft Tämperatur (min/max): '
                 f'{render_temperature(weather.temp_daily_min)} / '
                 f'{render_temperature(weather.temp_daily_max)}')
    )
    yield from check_aare_guru_weather_rain(
        rainfall=weather.rainfall,
        rain_risk=weather.rain_risk,
    )


register.check_plugin(
    name='aare_guru_weather_forecast',
    sections=['aare_guru_weather'],
    service_name='Wätter: i %s täg',
    discovery_function=discover_aare_guru_weather_forecast,
    check_function=check_aare_guru_weather_forecast,
)
