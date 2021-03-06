#
#                       ██           ██
#      ████            ░██          ░██
#     ██░░██  ██   ██ ██████  █████ ░██      ██████  ██████  ███     ██  ██████  █████  ██████
#    ░██ ░██ ░██  ░██░░░██░  ██░░░██░██████ ░░██░░█ ██░░░░██░░██  █ ░██ ██░░░░  ██░░░██░░██░░█
#    ░░█████ ░██  ░██  ░██  ░███████░██░░░██ ░██ ░ ░██   ░██ ░██ ███░██░░█████ ░███████ ░██ ░
#     ░░░░██ ░██  ░██  ░██  ░██░░░░ ░██  ░██ ░██   ░██   ░██ ░████░████ ░░░░░██░██░░░░  ░██
#        ░███░░██████  ░░██ ░░██████░██████ ░███   ░░██████  ███░ ░░░██ ██████ ░░██████░███
#        ░░░  ░░░░░░    ░░   ░░░░░░ ░░░░░   ░░░     ░░░░░░  ░░░    ░░░ ░░░░░░   ░░░░░░ ░░░
#
#
#
#
#                                             ██
#                                            ░██
#                    █████  ██   ██  ██████ ██████  ██████  ██████████
#                   ██░░░██░██  ░██ ██░░░░ ░░░██░  ██░░░░██░░██░░██░░██
#                  ░██  ░░ ░██  ░██░░█████   ░██  ░██   ░██ ░██ ░██ ░██
#                  ░██   ██░██  ░██ ░░░░░██  ░██  ░██   ░██ ░██ ░██ ░██
#                  ░░█████ ░░██████ ██████   ░░██ ░░██████  ███ ░██ ░██
#                   ░░░░░   ░░░░░░ ░░░░░░     ░░   ░░░░░░  ░░░  ░░  ░░
#
#
#
#
#          ██                  ██             ██   ██
#         ░██                 ░██            ░██  ░██
#         ░██  ██████   ██████░██  ██       ██████░██       █████  ██████████   █████
#      ██████ ░░░░░░██ ░░██░░█░██ ██       ░░░██░ ░██████  ██░░░██░░██░░██░░██ ██░░░██
#     ██░░░██  ███████  ░██ ░ ░████          ░██  ░██░░░██░███████ ░██ ░██ ░██░███████
#    ░██  ░██ ██░░░░██  ░██   ░██░██         ░██  ░██  ░██░██░░░░  ░██ ░██ ░██░██░░░░
#    ░░██████░░████████░███   ░██░░██        ░░██ ░██  ░██░░██████ ███ ░██ ░██░░██████
#     ░░░░░░  ░░░░░░░░ ░░░    ░░  ░░          ░░  ░░   ░░  ░░░░░░ ░░░  ░░  ░░  ░░░░░░
#
#
#  ▓▓▓▓▓▓▓▓▓▓
# ░▓ author ▓ ikigai
# ░▓ code   ▓ https://github.com/yedhink
# ░▓ mirror ▓
# ░▓▓▓▓▓▓▓▓▓▓
# ░░░░░░░░░░


# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'file://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'chrome://*/*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'qute://*/*')

## Definitions of search engines which can be used via the address bar.
## Maps a searchengine name (such as `DEFAULT`, or `ddg`) to a URL with a
## `{}` placeholder. The placeholder will be replaced by the search term,
## use `{{` and `}}` for literal `{`/`}` signs. The searchengine named
## `DEFAULT` is used when `url.auto_search` is turned on and something
## else than a URL was entered to be opened. Other search engines can be
## used by prepending the search engine name to the search term, e.g.
## `:open google qutebrowser`.
## Type: Dict
c.url.searchengines = {
        'DEFAULT': 'https://duckduckgo.com/?q={}',
        'i': 'https://duckduckgo.com/?q={}&iar=images&iax=images&ia=images',
        'vic': 'https://la.wikipedia.org/w/index.php?search={}&title=Specialis%3AQuaerere',
        'red': 'https://reddit.com/r/{}',
        'tpb': 'http://thepiratebay.org/search/{}',
        'andr': 'https://developer.android.com/develop/index.html?q={}',
        'ghr': 'https://github.com/search?utf8=%E2%9C%93&q={}&type=',
        'ghn': 'https://github.com/search?utf8=%E2%9C%93&q={}+in%3Aname&type=Repositories',
        'ud': 'https://www.urbandictionary.com/define.php?term={}&utm_source=search-action',
        'ddg': 'https://duckduckgo.com/?q={}&t=ha&iar=images',
        'aw': 'https://wiki.archlinux.org/index.php?title=Special%3ASearch&search={}',
        'yt': 'https://www.youtube.com/results?search_query={}',
        'w': 'https://www.wikipedia.org/search-redirect.php?family=wikipedia&language=en&search={}&language=en&go=Go',
        'sk': 'https://www.skytorrents.in/search/all/ed/1/?l=en-us&q={}',
        'whl': 'https://alpha.wallhaven.cc/search?q={}&categories=111&purity=100&sorting=views&order=desc',
        'whh': 'https://alpha.wallhaven.cc/search?q={}&categories=111&purity=100&atleast=2560x1440&sorting=views&order=desc&page=2',
        }

c.aliases = {
    'wh': "open -t https://alpha.wallhaven.cc/search?q=&categories=111&purity=100&topRange=1y&sorting=toplist&order=desc&colors=336600&page=1",
    'gh': "open -t https://github.com/yedhink",
    }

## Background color for webpages if unset (or empty to use the theme's
## color)
## Type: QtColor
c.colors.webpage.bg = 'black'

## How many commands to save in the command history. 0: no history / -1:
## unlimited
## Type: Int
c.completion.cmd_history_max_items = 100























