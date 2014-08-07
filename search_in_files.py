#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright © 2012 Xavier Manach <xav@tekio.org>

search_in_files is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Webinrest is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Webinrest. If not, see <http://www.gnu.org/licenses/>.


search_in_files is a text search python module.

The function search_in_text_files search a regexp in files, and return
the list files that's complain the regexp.
It's a folder resursive search by default.

"""

import os
import re
from magic import open as magic_open
from magic import MAGIC_MIME

magic_mime = magic_open(MAGIC_MIME)
magic_mime.load()


def recursion(expression, folder, files):
    results = []
    list_nodes = os.listdir(folder)
    for node_name in list_nodes:
        if node_name not in ['..', '.', '.git'] and \
                node_name[-1] != '~':
            if re.search(files, node_name):
                node_path = os.path.join(folder, node_name)
                if os.path.isdir(node_path):
                    results.extend(recursion(expression, node_path, files))
                else:
                    ctype = magic_mime.file(node_path)
                    if ctype.find('text/') != -1:
                        file_node = open(node_path)
                        data_node = file_node.read()
                        file_node.close()
                        if re.search(
                                expression, data_node,
                                flags=re.IGNORECASE):
                            results.append(node_path)
    return results


def search_in_text_files(expression, folder='.',
                         files='(.*)', recursive=True):
    results = []
    if os.path.exists(folder) and os.path.isdir(folder):
        list_nodes = os.listdir(folder)
        for node_name in list_nodes:
            if node_name not in ['..', '.', '.git'] and \
                    node_name[-1] != '~':
                if re.search(files, node_name):
                    node_path = os.path.join(folder, node_name)
                    if os.path.isdir(node_path):
                        if recursive:
                            results.extend(recursion(expression,
                                                     node_path, files))
                    else:
                        ctype = magic_mime.file(node_path)
                        if ctype.find('text/') != -1:
                            file_node = open(node_path)
                            data_node = file_node.read()
                            file_node.close()
                            if re.search(
                                    expression, data_node,
                                    flags=re.IGNORECASE):
                                results.append(node_path)
    return results
