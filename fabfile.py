from fabric.api import env, task, run
from fabric.context_managers import prefix

env.use_ssh_config=True
env.hosts = ['medmed']

contexts = {
    'domidoo': {
        'port': 8003,
        'virtualenv': 'domidooenv',
        'gunicorn_pid' : '~/domidoo-gunicorn-pid'
    }
}

def activate(context_name):
    return 'cd {0} && source bin/activate'.format(context_name)

@task
def build():
    context_name = 'domidoo'
    context = contexts[context_name]
    virtualenv = context['virtualenv']
    run('rm -fr {0}'.format(virtualenv))
    run('virtualenv {0}'.format(virtualenv))
    with prefix(activate(virtualenv)):
        run('git clone https://github.com/arialdomartini/domidoo.git')
        run('cd domidoo && pip install -r requirements.txt')
        run('cd domidoo/domidooweb && python setup.py develop')
        run('cd domidoo/domidooweb && alembic -n prod upgrade head')



@task
def start():
    context_name = 'domidoo'
    context = contexts[context_name]
    gunicorn_pid = context['gunicorn_pid']
    with prefix(activate(context['virtualenv'])):

        port = context['port']
        print "Starting the app on context ".format(context_name)
        run('gunicorn --daemon -p {0} -b 0.0.0.0:{1} --paster domidoo/domidooweb/production.ini'.format(gunicorn_pid, port))

@task
def stop():
    context_name = 'domidoo'
    context = contexts[context_name]
    port = context['port']
    gunicorn_pid = context['gunicorn_pid']
    with prefix(activate(context['virtualenv'])):
        print "Stopping the app on context ".format(context_name)
        run('kill -9 `cat {0}` && rm {0}'.format(gunicorn_pid))
