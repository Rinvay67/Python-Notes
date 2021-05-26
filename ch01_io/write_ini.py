from configparser import ConfigParser


config = ConfigParser()

config['default'] = {'IP': '192.168.14.2', 'PORT': '6072'}

config['custom'] = {}
config['custom']['user'] = 'admin'
config['custom']['password'] = '123456'

config['define'] = {}
sub_config = config['define']
sub_config['host'] = '192.168.14.2'
sub_config['port'] = '611'

config.add_section('key1')
config.set('key1', 'k1', '123456')
# config.remove_section('key1')
# config.remove_option('key1', 'k1')

with open('config.ini', 'w') as configfile:
    config.write(configfile)
