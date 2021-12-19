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
            # specify primary and secondary brand colors
            theme_hook.BRAND_COLORS: {
                theme_hook.PRIMARY: {
                    theme_hook.COLOR_V50: "#7a411b",
                    theme_hook.COLOR_V100: "#7a411b",
                    theme_hook.COLOR_V200: "#fdb813",
                    theme_hook.COLOR_V300: "#fdb813",
                    theme_hook.COLOR_V400: "#c9252b",
                    theme_hook.COLOR_V500: "#f15922",
                    theme_hook.COLOR_V600: "#60bb46",
                    theme_hook.COLOR_V700: "#60bb46",
                    theme_hook.COLOR_V800: "#6851a2",
                    theme_hook.COLOR_V900: "#6851a2",
                },
                theme_hook.SECONDARY: {
                    theme_hook.COLOR_V50: "#ffffd7",
                    theme_hook.COLOR_V100: "#ffffd7",
                    theme_hook.COLOR_V200: "#ffffd7",
                    theme_hook.COLOR_V300: "#ffffd7",
                    theme_hook.COLOR_V400: "#ffffd7",
                    theme_hook.COLOR_V500: "#ffffd7",
                    theme_hook.COLOR_V600: "#ffffd7",
                    theme_hook.COLOR_V700: "#ffffd7",
                    theme_hook.COLOR_V800: "#ffffd7",
                    theme_hook.COLOR_V900: "#ffffd7",
                },
            },
            # sign-in page config
            theme_hook.SIGN_IN: {
                theme_hook.BACKGROUND: static("background.jpg"),
                theme_hook.BACKGROUND_IMG_CREDIT: "Gerald Njoroge",
                theme_hook.SCRIM_OPACITY: 0.7,
                theme_hook.TITLE: "Young Scientists Kenya",
                theme_hook.TOP_LOGO: {
                    theme_hook.IMG_SRC: None,  # use default Kolibri bird
                    theme_hook.IMG_STYLE: "padding-left: 64px; padding-right: 64px; margin-bottom: 8px; margin-top: 8px",
                    theme_hook.IMG_ALT: None,
                },
                theme_hook.SHOW_POWERED_BY: True,
                theme_hook.SHOW_TITLE: True,
                theme_hook.SHOW_K_FOOTER_LOGO: True,
            },
            # side-nav config
            theme_hook.SIDE_NAV: {
                theme_hook.TITLE: "YSK",
                theme_hook.BRANDED_FOOTER: {},
                theme_hook.SHOW_K_FOOTER_LOGO: True,
            },
            # app bar config
            theme_hook.APP_BAR: {theme_hook.TOP_LOGO: None},
        }
