import click
import recastapi.request

def request_fmt():
  fmt =\
'''\
========================
RECAST request -- {uuid}
------------------------
Title: {title}
Requestor: {requestor}
Status: {status}\
'''
  return fmt


@click.group()
def cli():
    pass

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
