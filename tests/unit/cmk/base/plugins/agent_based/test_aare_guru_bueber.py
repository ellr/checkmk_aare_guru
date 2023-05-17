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

from cmk.base.plugins.agent_based.aare_guru_bueber import SwimmingPassage, parse_aare_guru_bueber


SECTION_1: SwimmingPassage = SwimmingPassage(
    state='closed',
    state_open_flag=False,
)


@pytest.mark.parametrize(
    "string_table, expected_section",
    [
        (
            [
                ['{"state": "closed", "state_open_flag": false, "source": "badmeister", "time": 1663653604}'],
            ],
            SECTION_1,
        ),
    ],
)
def test_parse_aare_guru_bueber(string_table: List[List[str]], expected_section: SwimmingPassage) -> None:
    assert parse_aare_guru_bueber(string_table) == expected_section
