import setuptools
try:  # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:  # for pip <= 9.0.3
    from pip.req import parse_requirements

install_reqs = parse_requirements('requirements.txt', session='hack')
reqs = [str(ir.req) for ir in install_reqs]


setuptools.setup(
    name='flaskcli3000',
    version='0.1',
    scripts=['./flaskcli3000/main.py'],
    author='Diego Pisani',
    description='Gadzoooks!',
    packages=['flaskcli3000'],
    install_requires=reqs,
    python_requires='>=3.5'
)