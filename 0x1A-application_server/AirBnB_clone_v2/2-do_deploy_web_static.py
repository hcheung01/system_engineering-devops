#!/usr/bin/python3
"""
Frabic module
"""
from fabric.api import *
from datetime import datetime
import os
env.hosts = ["35.243.155.238", "34.73.31.23"]
env.user = 'ubuntu'
env.key_filename = '~/.ssh/codingschool'


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


def do_deploy(archive_path):
    """deploy tar package to remote server"""

    if not os.path.exists(archive_path) and not os.path.isfile(archive_path):
        return False
    try:
        put(archive_path, "/tmp")
        fileonly = os.path.basename(archive_path)
        filename = os.path.splitext(fileonly)[0]
        run("mkdir -p /data/web_static/releases/{}/".format(filename))
        from_here = "/tmp/{}".format(fileonly)
        to_here = "/data/web_static/releases/{}/".format(filename)
        run("tar -xzf {} -C {}".format(from_here, to_here))
        run('rm /tmp/{}'.format(fileonly))
        run('mv {}web_static/* {}'.format(to_here, to_here))
        run('rm -rf {}web_static'.format(to_here))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(to_here))
        print('New version deployed!')
        return True
    except:
        return False
    return True
