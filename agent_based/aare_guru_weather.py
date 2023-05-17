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

from pydantic import BaseModel, Field

from .agent_based_api.v1 import register


class WeatherCurrent(BaseModel):
    air_temperature: float = Field(..., alias="tt")
    rainfall: float = Field(..., alias="rrreal")


class WeatherTodayDetail(BaseModel):
    air_temperature: float = Field(..., alias="tt")
    rainfall: int = Field(..., alias="rr")
    rain_risk: int = Field(..., alias="rrisk")
    weather_text: str = Field(..., alias="syt")


class WeatherToday(BaseModel):
    vormittag: WeatherTodayDetail = Field(..., alias="v")
    namitag: WeatherTodayDetail = Field(..., alias="n")
    abe: WeatherTodayDetail = Field(..., alias="a")


class WeatherForecast(BaseModel):
    day: str
    weather_text: str = Field(..., alias="syt")
    temp_daily_min: float = Field(..., alias="tn")
    temp_daily_max: float = Field(..., alias="tx")
    rainfall: int = Field(..., alias="rr")
    rain_risk: int = Field(..., alias="rrisk")


class Weather(BaseModel):
    current: WeatherCurrent
    today: WeatherToday
    forecast: list[WeatherForecast]


def parse_aare_guru_weather(string_table) -> Weather:
    if len(string_table) != 1:
        raise ValueError(f'section <<<aare_guru_weather>>> must be a single line but is {len(string_table)} lines')

    raw: dict = json.loads(string_table[0][0])
    return Weather.parse_obj(raw)


register.agent_section(
    name='aare_guru_weather',
    parse_function=parse_aare_guru_weather,
)
