

class Inifile(object):
    def __init__(self, inistr=None):
        self._cp = cp = SafeConfigParser(inline_comment_prefixes=['!'])

        # Preserve case
        cp.optionxform = str

        if inistr:
            cp.read_string(inistr)

        @staticmethod
        def load(file):
            if isinstance(file, str):
                file = open(file)

            return Inifile(file.read())
