#!/usr/bin/env python3

# Standard libraries
import codecs
import os
import sys
import io

# Parsing and serializing
import yaml
import toml

"""
yaml2toml - Convert YaML to ToML

Copyright 2021 Daniel F. Dickinson

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

---------------------------------------------------------------------------

Tested with Python 3.9.4 (Windows) and 3.8.6 (Ubuntu Linux)

"""


# Configuration
def read_yaml_config(config_name):
    config_yaml_file = io.open(config_name, "r", encoding="utf-8")
    config = yaml.safe_load(config_yaml_file)
    config_yaml_file.close()
    return config


def write_toml_config(config, config_name):
    config_toml_file = codecs.open(
        os.path.splitext(config_name)[0] + ".toml",
        "w",
        encoding="utf-8",
    )
    toml.dump(config, config_toml_file)
    config_toml_file.close()


def main():

    if len(sys.argv) != 2:
        raise ValueError("Missing filename")

    config_name = sys.argv[1]

    print("Converting " + str(config_name))
    config = read_yaml_config(config_name)
    write_toml_config(config, config_name)
    print("Done.")


if __name__ == "__main__":
    main()
