# WordPress eXtended RSS to Static Generator Convertor

## Overview

Python3 program to convert WordPress XML Export (WPXR) format file to [Hugo](https://gohugo.io) Markdown files (with YAML metadata).

The latest version can be downloaded from <https://git.wildtechgarden.ca/danielfdickinson/wpxr-to-static> or <https://github.com/danielfdickinson/wpxr-to-static>.

This program is called wpxr-to-static because it is hoped (but not tested) that one could convert to other static generation systems simply by modifying the data models in the configuration files.

## Acknowledgements

Inspired by ["ExitWP for Hugo" by Arjan Wooning](https://github.com/wooni005/exitwp-for-hugo), which was a port of [Thomas Frössman's ExitWP tool (for Jekyll)](https://github.com/some-programs/exitwp). wpxr-to-static is not a port of "ExitWP for Hugo", but a completely new program. However, "ExitWP for Hugo" served as an excellent educational guide and testbed for understanding the ElementTree (Python standard library module used to parse the WPXR file) result of parsing the WPXR file as well as the internal tree structure created by parsing the 'config.yaml' file.

## Using

FIXME: Add actual documentation of configuration and use.

## Dependencies

- Python 3.7?, 3.8, or 3.9 (lower Python 3.x _may_ work but are untested).
- markdownify
- PyYAML
- toml

## License

wpxr-to-static - WordPress eXtended RSS to Static Generator Convertor

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
