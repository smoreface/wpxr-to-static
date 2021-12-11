# WordPress eXtended RSS to Static Site Generator Conversion

## Overview

Python3 program to convert WordPress XML Export (WPXR) format files to [Hugo](https://gohugo.io) Markdown files (with YAML metadata).

The latest version can be downloaded from <https://github.com/danielfdickinson/wpxr-to-static>.

This program is called wpxr-to-static because it is hoped (but not tested) that one could convert to other static generation systems simply by modifying the data models in the configuration files.

## Acknowledgements

Inspired by ["ExitWP for Hugo" by Arjan Wooning](https://github.com/wooni005/exitwp-for-hugo), which was a port of [Thomas Frössman's ExitWP tool (for Jekyll)](https://github.com/some-programs/exitwp). wpxr-to-static is not a port of "ExitWP for Hugo", but a completely new program. However, "ExitWP for Hugo" served as an excellent educational guide and testbed for understanding the ElementTree (Python standard library module used to parse the WPXR file) result of parsing the WPXR file as well as the internal tree structure created by parsing the 'config.yaml' file.

## Dependencies

- Python 3.8 or 3.9 (lower Python 3.x _may_ work but are untested).
- html5lib
- markdownify
- PyYAML
- toml
- urllib3

## Using

### "Install"

#### Obtain the Program: Option 1 (Archive)

Download a ZIP file containing the Python script from [Github](https://github.com/danielfdickinson/wpxr-to-static/archive/refs/tags/0.2.0-alpha.7.zip) or download a .tar.gz file containing the Python script from [Github](https://github.com/danielfdickinson/wpxr-to-static/archive/refs/tags/0.2.0-alpha.7.tar.gz)

#### Obtain the Program: Option 2 (Git clone)

Clone the source from [WPXR by Daniel F. Dickinson on Github](https://github.com/danielfdickinson/wpxr-to-static)
```
git clone https://github.com/danielfdickinson/wpxr-to-static.git
```

#### Obtain the Dependencies

In the directory resulting from extracting the .zip or the .tar.gz, or from cloning, issue:

```
pip install --user -r requirements.txt
```

### Configure

Copy ``config.yaml`` from the extracted .zip or .tar.gz, or cloned directory, to a convenient location.

If you need to change the 'data model' you can also copy ``hugo_data_model.yaml`` to a location of your choice (not necessarily the same as ``config.yaml``)

As the comments in ``config.yaml`` indicate, the defaults are present in the ``config.yaml`` as commented out entries.  One only needs to uncomment lines if one needs to change from the default.

#### Some Configuration Settings of Particular Interest

``data_models``: A configuration file defining the mapping of the WPXR XML tags and contents to an intermediate form used to create a combination of YAML frontmatter and Markdown files for each post or page, and a config.toml for the site.

``wpxr_file``: Sets the location and name of the source WPXR (WordPress Xml) file.

``build_dir``: Where output is stored (aka target dir). If relative, is relative to the current working directly when you execute ``wpxr-to-static``.

``download_content_images``: Whether to downloads images from the WordPress site into the target directory.

``image_origin_local_path``: If set, ``wpxr-to-static`` will first look here for an image file and only download the image if is not already present. Downloads are placed in this path.

``item_type_filter``: A YAML _list_ of item types (as defined later) to exclude from output.

``rename_files``: A YAML _map_ of ``target-field-name: original-field-name`` pairs

``fields_value_replace``: A YAML _map_ of _maps_ that lists ``fields`` with maps of ``regexp-to-replace: regexp-substitution`` pairs.

#### Data Model Definition

TBD

### Execute

**NB**: A configuration file and data model in the location specified in the config file are required.
#### Option 1: config.yaml in Current Directory

Linux:
```bash
/path/to/wpxr-to-static.py
```

Windows:
```
C:\path\to\wpxr-to-static.py
```

**NB** Instead of config.yaml one can also use config.toml.
#### Option 2: config.yaml in another location

Linux:
```bash
/path/to/wpxr-to-static.py /another/path/to/config.yaml
```

Windows:
```
C:\path\to\wxpr-to-static.py C:\another\path\to\config.yaml
```

**NB**: You can substitute any ``name.yaml`` or ``name.toml`` for ``config.yaml``.

## Extras

``yaml2toml.py`` is a very simple YAML to TOML converter.

## License

wpxr-to-static - WordPress eXtended RSS to Static Site Generator Conversion

Copyright 2021 Daniel F. Dickinson

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
