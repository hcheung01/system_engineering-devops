#!/usr/bin/python3
"""
Frabic module
"""
from fabric.api import *
from datetime import datetime


def do_pack():
    """pack directory tar format to another directory"""

    local('mkdir -p versions')
    format_time = datetime.now().strftime('%Y%m%d%H%M%S')
    filepath = 'versions/web_static_{}.tgz'.format(format_time)
    cmd = "tar -cvzf {} web_static/".format(filepath)
    try:
        local(cmd, capture=True)
        return filepath
    except:
        return None
