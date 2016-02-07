# Package: did_you_client.config
import os.path

from configparser import ConfigParser


class DidYouConfig(object):

    default_values = {'default': {'host': '127.0.0.1',
                                  'request_port': '5555',
                                  'subscription_port': '5556'},
                      'checker': {'sleep_period': '600'}}

    def __init__(self, configuration_file):
        if not os.path.exists(configuration_file):
            self._write_default_config_file(configuration_file)
        config = ConfigParser()
        config.read(configuration_file)
        self._default_section = config['default']
        self._checker_section = config['checker']

    def _write_default_config_file(self, filename):
        config = ConfigParser()
        for section, options in self.default_values.items():
            config.add_section(section)
            for key, value in options.items():
                config.set(section, key, value)
        with open(filename, 'w') as config_file:
            config.write(config_file)

    @property
    def host(self):
        return self._default_section['host']

    @property
    def subscription_port(self):
        return self._default_section['subscription_port']

    @property
    def request_port(self):
        return self._default_section['request_port']

    @property
    def sleep_period(self):
        return self._checker_section['sleep_period']
