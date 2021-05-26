from configparser import ConfigParser


config = ConfigParser()

config.read('config.ini')
print(config.sections())

options = config.options('custom')
print(options)

value1 = config['custom']['user']
print(value1)
value2 = config.get('custom', 'user')
print(value2)

items = config.items('default')
print(items)

for key in config['default']:
    print(key)
