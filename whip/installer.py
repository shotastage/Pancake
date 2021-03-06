#
# Copyright (c) 2017 Shota Shimazu
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


from pancake.core import file
from pancake import console
import subprocess


def install(git_url):

    home_dir = file.homeDirectory()


    # Make directory if not exist
    if not (file.exists(home_dir + "./pancake_maples")):
        file.mkdir(home_dir + "./pancake_maples")

    # Clone maple package via Git url.
    try:
        res = subprocess.check_call(["git",  "clone", git_url])
    except:
        console.log("Failed to clone " + git_url + "!" , withError = True)
        exit(1)
