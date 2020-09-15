import click
import os
from pathlib import Path
from distutils.dir_util import copy_tree


@click.group()
def flaskcli3000():
    """
        To be or not to be
    """

@click.option('-n', '--name', help='Name of API')
@click.option('-d', '--design', help='Design of API')
@click.option('-f', '--framework', help='Framework of API')
@click.option('-t', '--type', help='Type of API')
@flaskcli3000.command()
def create_api(name: str, design: str, framework: str, type: str):
    """Create api"""
    # TODO: validate design and framework options (ENUM)
    # TODO: choose mvc template (https://github.com/bamboo-yujiro/flask-mvc-sample? https://github.com/CharlyJazz/Flask-MVC-Template?)

    if name is None or name == '':
        name = 'sample_api'
    if framework is None or framework == '':
        framework = 'flask'
    if design is None or design == '':
        design = 'business'
    if type is None or type == '':
        type = 'rest'
    base_path = os.path.realpath(__file__)
    base_path = os.path.abspath(os.path.join(base_path, '..'))
    from_directory = os.path.join(base_path, 'base', 'api', framework, type, design)
    to_directory = os.path.join(os.getcwd())

    copy_tree(from_directory, to_directory)

    old_name = os.path.join(to_directory, 'sample_api')
    new_name = os.path.join(to_directory, name)
    os.rename(old_name, new_name)

    dotenv_path = os.path.join(new_name, '.env')
    Path(dotenv_path).touch()


if __name__ == '__main__':
    flaskcli3000(prog_name='flaskcli3000')