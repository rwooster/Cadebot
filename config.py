# Read keys from the config file

class Config:

    def __init__(self, config_file):
        self.filename = config_file

    def __getitem__(self, key):
        return self.__read_key(key)

    def __read_key(self, key):
        with open(self.filename) as f:
            for line in f:
                objkey, content = line.split("=", 1)
                if objkey == key:
                    # Remove trailing whitespace
                    return content.rstrip()

        raise StandardError("No content found for key {0}".format(key))

