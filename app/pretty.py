
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class pretty_print():
    def info(self, message):
        print("[+] Info:{}- {}{}".format(bcolors.OKGREEN, message, bcolors.ENDC))

    def warning(self, message):
        print("{}[-] Warning: {}{}".format(bcolors.WARNING, message, bcolors.ENDC))

    def critical(self, message):
        print("{}[-] Critical: {}{}".format(bcolors.FAIL, message, bcolors.ENDC))

    def header(self, message):
        print("{}{}{}".format(bcolors.HEADER, message, bcolors.ENDC))

pretty = pretty_print()