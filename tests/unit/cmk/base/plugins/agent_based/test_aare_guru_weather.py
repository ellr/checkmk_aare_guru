#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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

from typing import List, Tuple

import pytest

from cmk.base.plugins.agent_based.agent_based_api.v1 import Result, State, Metric

from cmk.base.plugins.agent_based.aare_guru_sun import Sun, SunData
from cmk.base.plugins.agent_based.aare_guru_weather import (
    parse_aare_guru_weather,
    Weather,
    WeatherCurrent,
    WeatherToday,
    WeatherTodayDetail,
    WeatherForecast,
)
from cmk.base.plugins.agent_based.aare_guru_weather_current import check_aare_guru_weather_current


SECTION_SUN: Sun = Sun(
    today=SunData(
        suntotal='12:44',
        sunrelative=81,
    )
)


SECTION_WEATHER: Weather = Weather(
    current=WeatherCurrent(tt=14.8, rrreal=0.2),
    today=WeatherToday(
        v=WeatherTodayDetail(tt=16.0, rr=0, rrisk=0, syt='bewöukt'),
        n=WeatherTodayDetail(tt=17.0, rr=2, rrisk=90, syt='e gutsch'),
        a=WeatherTodayDetail(tt=15.0, rr=13, rrisk=90, syt='starche räge')
    ),
    forecast=[
        WeatherForecast(day='Mitwuch', syt='e gutsch', tn=10.0, tx=14.0, rr=5, rrisk=90),
        WeatherForecast(day='Donschti', syt='e gutsch', tn=5.0, tx=14.0, rr=2, rrisk=70),
        WeatherForecast(day='Friti', syt='e gutsch', tn=7.0, tx=13.0, rr=2, rrisk=70),
        WeatherForecast(day='Samschti', syt='bewöukt', tn=7.0, tx=15.0, rr=1, rrisk=30),
    ]
)


@pytest.mark.parametrize(
    "string_table, expected_section",
    [
        (
            [
                ['{"current": {"tt": 14.8, "rr": 1, "rrreal": 0.2, "timestamp": 1683646200, "timestring": "17:30"}, '
                 '"today": {"v": {"sy": "c", "syt": "bew\u00f6ukt", "symt": 3, "tt": 16, "rr": 0, "rrisk": 0}, "n": '
                 '{"sy": "j", "syt": "e gutsch", "symt": 10, "tt": 17, "rr": 2, "rrisk": 90}, "a": {"sy": "f", '
                 '"syt": "starche r\u00e4ge", "symt": 6, "tt": 15, "rr": 13, "rrisk": 90}}, "forecast": '
                 '[{"day": "Mitwuch", "dayshort": "Mi.", "timestamp": 1683734300, "sy": "j", "syt": "e gutsch", '
                 '"symt": 10, "tx": 14, "tn": 10, "rr": 5, "rrisk": 90}, {"day": "Donschti", "dayshort": "Do.", '
                 '"timestamp": 1683820700, "sy": "j", "syt": "e gutsch", "symt": 10, "tx": 14, "tn": 5, "rr": 2, '
                 '"rrisk": 70}, {"day": "Friti", "dayshort": "Fr.", "timestamp": 1683907100, "sy": "j", "syt": "e gutsch", '
                 '"symt": 10, "tx": 13, "tn": 7, "rr": 2, "rrisk": 70}, {"day": "Samschti", "dayshort": "Sa.", '
                 '"timestamp": 1683993500, "sy": "c", "syt": "bew\u00f6ukt", "symt": 3, "tx": 15, "tn": 7, "rr": 1, '
                 '"rrisk": 30}]}'],
            ],
            SECTION_WEATHER,
        ),
    ],
)
def test_parse_aare_guru_weather(string_table: List[List[str]], expected_section: Weather) -> None:
    assert parse_aare_guru_weather(string_table) == expected_section


@pytest.mark.parametrize(
    "section_weather, section_sun, expected_check_result",
    [
        (
            SECTION_WEATHER,
            SECTION_SUN,
            (
                Result(state=State.OK, summary='Luft Tämperatur: 14.8 °C'),
                Metric('temperature', 14.8),
                Result(state=State.OK, summary='Räge: 0.2 mm/10min'),
                Metric('rainfall', 0.2),
                Result(state=State.OK, summary='Sunnestunge: 12:44'),
            ),
        ),
    ],
)
def test_check_aare_guru_aare_forecast(section_weather: Weather, section_sun: Sun, expected_check_result: Tuple) -> None:
    assert tuple(check_aare_guru_weather_current(section_weather, section_sun)) == expected_check_result
