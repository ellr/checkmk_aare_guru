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

from cmk.base.plugins.agent_based.aare_guru_aare import Aare, parse_aare_guru_aare


SECTION_1: Aare = Aare(
    location="B\u00e4rn",
    timestamp=1683646800,
    temperature=12.8,
    temperature_prec=12.83,
    temperature_text="Las vilech gschider lasii",
    temperature_text_short="Gschider la si",
    flow=261,
    flow_text="\u26a0\ufe0f mega viu",
    forecast2h=12.8,
    forecast2h_text="Blibt \u00e4u\u00e4 \u00f6pe glich",
)


@pytest.mark.parametrize(
    "string_table, expected_section",
    [
        (
            [
                ['{"location": "B\u00e4rn", "location_long": "Bern, Sch\u00f6nau", "coordinates": '
                 '{"lat": 46.93, "lon": 7.45}, "forecast": false, "timestamp": 1683646800, "timestring": "17:40", '
                 '"temperature": 12.8, "temperature_prec": 12.83, "temperature_text": "Las vilech gschider lasii", '
                 '"temperature_text_short": "Gschider la si", "flow": 261, "flow_text": "\u26a0\ufe0f mega viu", '
                 '"forecast2h": 12.8, "forecast2h_text": "Blibt \u00e4u\u00e4 \u00f6pe glich", "temperature_scale": '
                 '[{"value": 1, "text": "Iglu boue bringts meh", "position": "start"}, {"value": 12, "text": "Las '
                 'vilech gschider lasii", "position": "start"}, {"value": 16, "text": "Viu chauts Wasser", "position": '
                 '"start"}, {"value": 17, "text": "Mit de Boumst\u00e4m schw\u00fcmme", "position": "start"}, '
                 '{"value": 18, "text": "R\u00e4cht gut. Mit viu Wasser", "position": "start"}, {"value": 19, '
                 '"text": "Es het mega schriis", "position": "start"}, {"value": 21, "text": "Es het megaviu schriis", '
                 '"position": "start"}, {"value": 22, "text": "Spaghettiwasser", "position": "start"}], "flow_scale": '
                 '[{"value": 50, "text": "nid viu", "position": "start"}, {"value": 100, "text": "eher wenig", '
                 '"position": "start"}, {"value": 150, "text": "ganz g\u00e4big", "position": "start"}, {"value": 200, '
                 '"text": "ender viu", "position": "start"}, {"value": 250, "text": "mega viu", "position": "start"}, '
                 '{"value": 300, "text": "brutal viu!", "position": "start"}, {"value": 360, "text": "extrem viu!", '
                 '"position": "start"}, {"value": 430, "text": "hochwasser!", "position": "start"}, {"value": 500, '
                 '"text": "mega hochwasser!", "position": "start"}, {"value": 560, "text": "jahrhunderthochwasser!", '
                 '"position": "start"}]}'],
            ],
            SECTION_1,
        ),
    ],
)
def test_parse_aare_guru_aare(string_table: List[List[str]], expected_section: Aare) -> None:
    assert parse_aare_guru_aare(string_table) == expected_section
