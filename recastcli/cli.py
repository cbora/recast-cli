import click
import recastapi.request
import recastapi.analysis

def request_fmt():
  fmt =\
u'''\
========================
RECAST request -- {uuid}
------------------------
Title: {title}
Requestor: {requestor}
Status: {status}\
'''
  return fmt

def analysis_fmt():
  fmt =\
u'''\
========================
RECAST analysis -- {title}
------------------------
UUID: {uuid}
Collaboration: {collaboration}
# of requests: {number_of_requests}\
'''
  return fmt

@click.group()
def cli():
    pass

@cli.command(name = 'list-analyses')
def list_analyses():
    for p in recastapi.analysis.analysis():
      click.echo(analysis_fmt().format(**p))

@cli.command(name = 'list-analysis')
@click.argument('uuid')
def list_analysis(uuid):
  click.echo(analysis_fmt().format(**recastapi.analysis.analysis(uuid)))


@cli.command(name = 'list-requests')
def list_requests():
    for p in recastapi.request.request():
      print request_fmt().format(**p)

@cli.command(name = 'list-request')
@click.argument('uuid')
def list_request(uuid):
    fmt =\
'''\
========================
RECAST request -- {uuid}
------------------------
Title: {title}
Requestor: {requestor}
Status: {status}\
'''
    print request_fmt().format(**recastapi.request.request(uuid))
