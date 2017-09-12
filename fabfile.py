from fabric.api import  env,run
from fabric.operations import sudo

GIT_REPO = 'https://github.com/Lieeber/blogProject.git'

env.user = 'lieeber'
env.password = 'lieeber'
env.hosts = ['www.lieeber.com']
env.port = '22'


def deploy():
    source_folder = '/home/lieeber/sites/www.barrylee.top/myBlog'

    run('cd %s && git pull' % source_folder)
    run("""
        cd {} &&
        ../env/bin/pip install -r requirements.txt &&
        ../env/bin/python3 manage.py collectstatic --noinput &&
        ../env/bin/python3 manage.py migrate
        """.format(source_folder))
    sudo('restart gunicorn-www.barrylee.top')
    sudo('service nginx reload')