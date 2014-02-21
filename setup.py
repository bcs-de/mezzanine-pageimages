#
#   Copyright 2013 by Arnold Krille for bcs kommunikationsloesungen
#                     <a.krille@b-c-s.de>
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#

from setuptools import setup

setup(
    name="mezzanine-pageimages",
    version="0.2.3",
    description="Define (background-/banner-)images per page in mezzanine.",
    long_description=open('README.md', 'r').read(),
    author="Arnold Krille for bcs kommunikationsloesungen",
    author_email="a.krille@b-c-s.de",
    url="http://github.com/bcs-de/mezzanine-pageimages",
    license=''
    'Licensed under the Apache License, Version 2.0 (the "License");\n'
    'you may not use this file except in compliance with the License.\n'
    'You may obtain a copy of the License at\n'
    '\n'
    '  http://www.apache.org/licenses/LICENSE-2.0\n'
    '\n'
    'Unless required by applicable law or agreed to in writing, software\n'
    'distributed under the License is distributed on an "AS IS" BASIS,\n'
    'WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n'
    'See the License for the specific language governing permissions and\n'
    'limitations under the License.',

    packages=['pageimages', 'pageimages.templatetags', 'pageimages.migrations'],
    install_requires=['mezzanine>=3.0.0'],
)
