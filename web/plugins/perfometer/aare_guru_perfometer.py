#!/usr/bin/python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-

"""aare_guru perfometer definitions

Authors:    Roger Ellenberger <roger.ellenberger@wagner.ch>
"""

from cmk.gui.plugins.metrics import perfometer_info


perfometer_info.append({
    "type": "logarithmic",
    "metric": "temperature",
    "half_value": 20,
    "exponent": 2,
})

perfometer_info.append({
    "type": "logarithmic",
    "metric": "water_flow",
    "half_value": 200,
    "exponent": 2,
})

perfometer_info.append({
    "type": "linear",
    "segments": ["rain_risk"],
    "total": 100.0,
})