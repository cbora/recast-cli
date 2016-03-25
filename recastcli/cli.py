import click
import recastapi.request
import recastapi.analysis
import recastapi.user

def request_fmt():
  fmt =\
u'''\
========================
RECAST request -- {uuid}
------------------------
reason for request: {reason_for_request}
additional information: {additional_information}
Status: {status}
post date: {post_date}
\n\
'''
  return fmt

def analysis_fmt():
  fmt =\
u'''\
========================
RECAST analysis -- {title}
------------------------
id: {id}
Collaboration: {collaboration}
description: {description}
\n\
'''
  return fmt

def user_fmt():
  fmt =\
u'''\
==================================
RECAST user -- {name}
----------------------------------
email: {email}
orcid_id: {orcid_id}\
'''
  return fmt

@click.group()
def cli():
    pass

@cli.command(name = 'list-users')
def list_users():
  for p in recastapi.user.user()['_items']:
    click.echo(user_fmt().format(**p))

@cli.command(name = 'list-analyses')
def list_analyses():
  for p in recastapi.analysis.analysis()['_items']:
    click.echo(analysis_fmt().format(**p))

@cli.command(name = 'list-analysis')
@click.argument('uuid')
def list_analysis(uuid):
  click.echo(analysis_fmt().format(**recastapi.analysis.analysis(uuid)))

@cli.command(name = 'list-requests')
def list_requests():
    for p in recastapi.request.request()['_items']:
      print request_fmt().format(**p)

@cli.command(name = 'list-request')
@click.argument('uuid')
def list_request(uuid):
  print request_fmt().format(**recastapi.request.request(uuid))

@cli.command(name = 'add-analysis')
@click.argument('title', 'description')
def add_analysis(title, description, collaboration,
                 e_print, journal, doi, inspire_url,
                 run_condition_id):
  recastapi.analysis.create(title=title, description=description,
                            collaboration=collaboration, e_print=e_print,
                            journal=journal, doi=doi, inspire_url=inspire_url,
                            run_condition_id=run_condition_id)
                            

@cli.command(name= 'add-request')
@click.argument('reason_for_request'):
