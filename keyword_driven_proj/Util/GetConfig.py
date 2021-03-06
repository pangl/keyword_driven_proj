import configparser

class Config(object):

    def __init__(self,config_file_path):
        self.config_file_path = config_file_path
        self.config = configparser.ConfigParser()
        self.config.read(self.config_file_path)

    def get_all_sections(self):
        return self.config.sections()

    def get_option(self,section_name,option_name):
        value = self.config.get(section_name,option_name)
        return value

    def all_section_items(self,section_name):
        items = self.config.items(section_name)
        print(items)
        return dict(items)
