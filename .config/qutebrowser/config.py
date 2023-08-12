# general settings
config.load_autoconfig()
c.hints.border = "1px solid #dcdcdc"
c.hints.mode = "letter"
c.hints.chars = "asdfghjkl"
c.hints.min_chars = 1
c.zoom.default = "75%"

# colors
c.colors.hints.fg = "#121317"
c.colors.hints.bg = "#dcdcdc"

# fonts
c.fonts.default_family = ["DejaVu Sans Mono"]
c.fonts.tabs.selected = "9pt DejaVu Sans Mono"
c.fonts.tabs.unselected = "9pt DejaVu Sans Mono"
c.fonts.hints = "9pt DejaVu Sans Mono"
c.fonts.keyhint = "9pt DejaVu Sans Mono"
c.fonts.prompts = "9pt DejaVu Sans Mono"
c.fonts.downloads = "9pt DejaVu Sans Mono"
c.fonts.statusbar = "9pt DejaVu Sans Mono"
c.fonts.contextmenu = "9pt DejaVu Sans Mono"
c.fonts.messages.error = "9pt DejaVu Sans Mono"
c.fonts.messages.info = "9pt DejaVu Sans Mono"
c.fonts.messages.warning = "9pt DejaVu Sans Mono"
c.fonts.debug_console = "9pt DejaVu Sans Mono"
c.fonts.completion.entry = "9pt DejaVu Sans Mono"
c.fonts.completion.category = "9pt DejaVu Sans Mono"

# video playback
# option to open a video in mpv, pressing Ctrl+/ will bring up all
# the available video links on the page, then press a corresponding
# key combination for the video link require and will play with mpv
config.bind('<Ctrl+/>', 'hint links spawn --detach mpv {hint-url}')

# colors
c.colors.completion.fg = "#dcdcdc"
c.colors.completion.category.fg = "#dcdcdc"
c.colors.completion.category.bg = "#121317"
c.colors.completion.item.selected.fg = "#dcdcdc"
c.colors.completion.item.selected.match.fg = "#dcdcdc"
c.colors.completion.item.selected.bg = "#121317"
c.colors.completion.item.selected.border.top = "#121317"
c.colors.completion.item.selected.border.bottom = "#121317"
c.colors.completion.match.fg = "#dcdcdc"
c.colors.statusbar.normal.fg = "#dcdcdc"
c.colors.statusbar.normal.bg = "#121317"
c.colors.statusbar.insert.fg = "#dcdcdc"
c.colors.statusbar.insert.bg = "#121317"
c.colors.statusbar.command.bg = "#121317"
c.colors.statusbar.command.fg = "#dcdcdc"
c.colors.statusbar.caret.bg = "#121317"
c.colors.statusbar.caret.selection.fg = "#dcdcdc"
c.colors.statusbar.progress.bg = "#121317"
c.colors.statusbar.passthrough.bg = "#dcdcdc"
c.colors.statusbar.url.fg = "#dcdcdc"
c.colors.statusbar.url.success.http.fg = "#dcdcdc"
c.colors.statusbar.url.success.https.fg = "#dcdcdc"
c.colors.statusbar.url.error.fg = "#121317"
c.colors.statusbar.url.warn.fg = "#dcdcdc"
c.colors.statusbar.url.hover.fg = "#dcdcdc"
c.colors.tabs.bar.bg = "#121317"
c.colors.tabs.even.fg = "#dcdcdc"
c.colors.tabs.even.bg = "#121317"
c.colors.tabs.odd.fg = "#dcdcdc"
c.colors.tabs.odd.bg = "#121317"
c.colors.tabs.selected.even.fg = "#dcdcdc"
c.colors.tabs.selected.even.bg = "#121317"
c.colors.tabs.selected.odd.fg = "#dcdcdc"
c.colors.tabs.selected.odd.bg = "#121317"
c.colors.tabs.indicator.start = "#121317"
c.colors.tabs.indicator.stop = "#121317"
c.colors.tabs.indicator.error = "#121317"
c.colors.downloads.start.fg = "#dcdcdc"
c.colors.downloads.start.bg = "#121317"
c.colors.downloads.stop.fg = "#dcdcdc"
c.colors.downloads.stop.bg = "#121317"
c.colors.keyhint.fg = "#dcdcdc"
c.colors.keyhint.suffix.fg = "#dcdcdc"
c.colors.keyhint.bg = "#121317"
c.colors.messages.error.bg = "#121317"
c.colors.messages.error.border = "#121317"
c.colors.messages.warning.bg = "#121317"
c.colors.messages.warning.border = "#121317"
c.colors.messages.info.bg = "#121317"
c.colors.prompts.fg = "#dcdcdc"
c.colors.prompts.bg = "#121317"
c.colors.prompts.selected.bg = "#121317"
