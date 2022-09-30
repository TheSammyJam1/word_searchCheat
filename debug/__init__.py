from colorama import init
from colorama import Fore, Style
init()
Info = Fore.BLUE +    '[INFO]    - '
Normal = Fore.GREEN + '[NORMAL]  - '
Warn = Fore.YELLOW +  '[WARNING] - '
Error = Fore.RED +    '[ERROR]   - '

debug = False


def debug_on():
    global debug
    debug = True
    debug_print('text debug ACTIVATED', Info)


def debug_off():
    global debug
    debug = False
    debug_print('text debug DEACTIVATED', Info)


def debug_print(text, status=Normal):
    if debug:

        print(status + str(text) + Style.RESET_ALL)