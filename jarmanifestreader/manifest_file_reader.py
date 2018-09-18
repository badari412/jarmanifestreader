from __future__ import print_function

import os
import zipfile


def _get_manifest_file_contents(jar_file_path):
    with zipfile.ZipFile(jar_file_path) as z:
        return z.open('META-INF/MANIFEST.MF').readlines()


def _format_attributes(manifest_file_contents):
    manifest_contents = {}
    for attribute in [a.decode('utf-8') for a in manifest_file_contents]:
        try:
            manifest_contents[attribute.split(':')[0].strip()] = attribute.split(':')[1].strip()
        except IndexError:
            continue
    return manifest_contents


def _is_valid_jar_file(jar_file_path):
    if jar_file_path == '' or jar_file_path is None:
        raise Exception('jar_file_path should not be empty. Please supply the path of the jar file.')

    if not os.path.exists(jar_file_path):
        raise Exception(jar_file_path + ' file does not exist. Please provide correct path.')

    if not jar_file_path.endswith('.jar'):
        raise Exception(jar_file_path + ' file is not a jar file. Please provide a jar file path.')


def get_manifest_contents(jar_file_path):
    """
    Returns the contents of the manifest file of the given jar file in dictionary format
    :param jar_file_path: path of the jar file
    :return: Return s a dictionary of the manifets file contents
    """
    _is_valid_jar_file(jar_file_path)
    manifest_file_contents = _get_manifest_file_contents(jar_file_path)
    return _format_attributes(manifest_file_contents)


def print_manifest_contents(jar_file_path):
    """
    Prints the contents of the manifest file of the given jar file in dictionary format
    :param jar_file_path:
    :return:
    """
    print(get_manifest_contents(jar_file_path))
