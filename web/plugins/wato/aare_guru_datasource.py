#!/usr/bin/python3
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
WATO Rulespec for datasource program Aare Guru
This file is written for Check_MK.

Authors:    Roger Ellenberger <roger.ellenberger@wagner.ch>
"""

from cmk.gui.i18n import _
from cmk.gui.plugins.wato.utils import (
    HostRulespec,
    rulespec_registry,
    HTTPProxyReference,
)
from cmk.gui.valuespec import (
    Tuple,
    TextAscii,
)
from cmk.gui.plugins.wato.datasource_programs import RulespecGroupDatasourceProgramsCustom


def _valuespec_special_agents_aare_guru():
    return Tuple(
        title=_("Aare Guru"),
        help=_("Activate monitoring of the the longest wholly Swiss river"),
        elements = [
            TextAscii(
                title=_("City"),
                allow_empty=False,
                default_value='bern',
            ),
            HTTPProxyReference(),
        ]
    )


rulespec_registry.register(
    HostRulespec(
        group=RulespecGroupDatasourceProgramsCustom,
        name='special_agents:aare_guru',
        valuespec=_valuespec_special_agents_aare_guru,
        match_type = "first",
        factory_default=HostRulespec.FACTORY_DEFAULT_UNUSED,
    ),
)
