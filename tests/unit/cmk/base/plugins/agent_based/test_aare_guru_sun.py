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

from typing import List

import pytest

from cmk.base.plugins.agent_based.aare_guru_sun import Sun, SunData, parse_aare_guru_sun


SECTION_1: Sun = Sun(
    today=SunData(
        suntotal='3:21',
        sunrelative=23,
    )
)


@pytest.mark.parametrize(
    "string_table, expected_section",
    [
        (
            [
                ['{"today": {"suntotal": "3:21", "sunrelative": 23}, '
                 '"forecast": {"1": {"day": "Mitwuch", "dayshort": "Mi.", "suntotal": "3:10", '
                 '"sunrelative": 22}, "2": {"day": "Donschti", "dayshort": "Do.", '
                 '"suntotal": "2:54", "sunrelative": 20}, "3": {"day": "Friti", "dayshort": "Fr.", '
                 '"suntotal": "3:15", "sunrelative": 22}, "4": {"day": "Samschti", "dayshort": "Sa.", '
                 '"suntotal": "4:16", "sunrelative": 29}}, "sunlocations": [{"name": "Eichholz", '
                 '"sunrise": 1683611460, "sunriselocal": "07:51", "sunset": 1683648660, '
                 '"sunsetlocal": "18:11", "timeleft": 763, "timeleftstring": "0:12:43"}, {"name": "Marzili", '
                 '"sunrise": 1683609540, "sunriselocal": "07:19", "sunset": 1683652260, '
                 '"sunsetlocal": "19:11", "timeleft": 4363, "timeleftstring": "1:12:43"}, '
                 '{"name": "Lorraine", "sunrise": 1683621120, "sunriselocal": "10:32", "sunset": 1683651060, '
                 '"sunsetlocal": "18:51", "timeleft": 3163, "timeleftstring": "0:52:43"}]}'],
            ],
            SECTION_1,
        ),
    ],
)
def test_parse_aare_guru_sun(string_table: List[List[str]], expected_section: Sun) -> None:
    assert parse_aare_guru_sun(string_table) == expected_section
