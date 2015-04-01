from setuptools import setup, find_packages

setup(
  name = 'recast-cli',
  description = 'command line interface for RECAST',
  version = '0.0.1',
  packages = find_packages(),
  author = 'Lukas Heinrich',
  entry_points={
        'console_scripts': ['recast-cli = recastcli.cli:cli']
      },
  install_requires = [
    'Click',
    'recast-api'
  ],
  dependency_links = [
      'https://github.com/lukasheinrich/recast-api/tarball/master#egg=recast-api-0.0.1'
  ]
)