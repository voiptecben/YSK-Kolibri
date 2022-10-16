from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

from django.templatetags.static import static

from kolibri.core import theme_hook
from kolibri.plugins import KolibriPluginBase
from kolibri.plugins.hooks import register_hook


class DefaultThemePlugin(KolibriPluginBase):
    pass


@register_hook
class DefaultThemeHook(theme_hook.ThemeHook):
    @property
    def theme(self):
        return {
            # primary and secondary brand colors
            "brandColors": {
                "primary": {
                    "v_50": "#7a411b",
                    "v_100": "#7a411b",
                    "v_200": "#fdb813",
                    "v_300": "#fdb813",
                    "v_400": "#c9252b",
                    "v_500": "#f15922",
                    "v_600": "#60bb46",
                    "v_700": "#60bb46",
                    "v_800": "#6851a2",
                    "v_900": "#6851a2",
                },
                "secondary": {
                    "v_50": "#ffffd7",
                    "v_100": "#ffffd7",
                    "v_200": "#ffffd7",
                    "v_300": "#ffffd7",
                    "v_400": "#ffffd7",
                    "v_500": "#ffffd7",
                    "v_600": "#ffffd7",
                    "v_700": "#ffffd7",
                    "v_800": "#ffffd7",
                    "v_900": "#ffffd7",
                },
            },
            "signIn": {
                "background": static("background.jpg"),
                "backgroundImgCredit": "Gerald Njoroge",
                "topLogo": {
                    "style": "padding-left: 64px; padding-right: 64px; margin-bottom: 8px; margin-top: 8px",
                },
            },
        }
