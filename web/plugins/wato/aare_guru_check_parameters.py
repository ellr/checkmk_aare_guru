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
WATO Rulespec for check parameters for Aare Guru checks
This file is written for Check_MK.

Authors:    Roger Ellenberger <roger.ellenberger@wagner.ch>
"""

from cmk.gui.i18n import _
from cmk.gui.plugins.wato.utils import (
    CheckParameterRulespecWithItem,
    rulespec_registry,
    RulespecGroupCheckParametersEnvironment,
)
from cmk.gui.valuespec import (
    Dictionary,
    Float,
    Integer,
    TextInput,
    Tuple,
)


def _parameter_valuespec_aare_guru_levels():
    return Dictionary(
        help=_(
            'To obtain the data required for this check, please configure'
            ' the datasource program "Aare Guru".'
        ),
        elements=[
            (
                "river_temperature_levels",
                Tuple(
                    title=_("Upper levels on river temperature"),
                    help=_(
                        "The levels will be used to alert if the river "
                        "temperature exceeds these levels."
                    ),
                    elements=[
                        Float(
                            title=_("Warning at"),
                            default_value=20.0,
                        ),
                        Float(
                            title=_("Critical at"),
                            default_value=22.0,
                        ),
                    ],
                ),
            ),
            (
                "air_temperature_levels",
                Tuple(
                    title=_("Upper levels on air temperature"),
                    help=_(
                        "The levels will be used to alert if the river "
                        "temperature exceeds these levels."
                    ),
                    elements=[
                        Float(
                            title=_("Warning at"),
                            default_value=25.0,
                        ),
                        Float(
                            title=_("Critical at"),
                            default_value=30.0,
                        ),
                    ],
                ),
            ),
            (
                "flow_levels_upper",
                Tuple(
                    title=_("Upper levels on water flow"),
                    help=_(
                        "The levels will be used to alert if the water "
                        "flow exceeds these levels."
                    ),
                    elements=[
                        Integer(
                            title=_("Warning at"),
                            minvalue=0,
                            default_value=200,
                        ),
                        Integer(
                            title=_("Critical at"),
                            minvalue=0,
                            default_value=240,
                        ),
                    ],
                ),
            ),
            (
                "flow_levels_lower",
                Tuple(
                    title=_("Lower levels on water flow"),
                    help=_(
                        "The levels will be used to alert if the water "
                        "flow fall below these levels."
                    ),
                    elements=[
                        Integer(
                            title=_("Warning at"),
                            minvalue=0,
                            default_value=100,
                        ),
                        Integer(
                            title=_("Critical at"),
                            minvalue=0,
                            default_value=50,
                        ),
                    ],
                ),
            ),
        ],
    )


rulespec_registry.register(
    CheckParameterRulespecWithItem(
        check_group_name="aare_guru_check_levels",
        group=RulespecGroupCheckParametersEnvironment,
        item_spec=lambda: TextInput(title=_("Aare Guru check levels")),
        match_type="dict",
        parameter_valuespec=_parameter_valuespec_aare_guru_levels,
        title=lambda: _("Aare Guru check levels"),
    )
)
