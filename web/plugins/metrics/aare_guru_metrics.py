"""aare_guru metric defintions

Colors for metric_info can be found here:
https://github.com/Checkmk/checkmk/blob/master/cmk/gui/plugins/metrics/utils.py#L342

Authors:    Roger Ellenberger <roger.ellenberger@wagner.ch>
"""

from cmk.gui.i18n import _
from cmk.gui.plugins.metrics import metric_info


metric_info["temperature"] = {
    "title": _("Tämperatur"),
    "unit": "count",
    "color": "22/a",
}

metric_info["water_flow"] = {
    "title": _("Wassermängi"),
    "unit": "count",
    "color": "35/a",
}

metric_info["rain_risk"] = {
    "title": _("Räge risiko"),
    "unit": "%",
    "color": "42/a",
}
