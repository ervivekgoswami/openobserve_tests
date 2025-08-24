import configparser
import os

cwd = os.getcwd()
this_folder = os.path.dirname(os.path.abspath(__file__))
init_file = os.path.join(cwd, 'pytest.ini')

config = configparser.ConfigParser()
config.read(init_file)