import click
import recastapi.request
import recastapi.analysis
import recastapi.user
import recastapi.response
import yaml
import os

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
@click.argument('data')
def add_analysis(data):

  read_config()
  if not os.path.isfile(data):
    click.echo('File does not exist!')
    return
  
  f = open(data)
  data_map = yaml.load(f)
  f.close()
  try:
    recastapi.analysis.create(title=data_map['title'],
                              collaboration=data_map['collaboration'],
                              e_print=data_map['e_print'],
                              journal=data_map['journal'],
                              doi=data_map['doi'],
                              inspire_url=data_map['inspire_url'],
                              description=data_map['description'],
                              run_condition_name=data_map['run_condition_name'],
                              run_condition_description=data_map['run_condition_description']
                              )
    click.echo('Successfully created the analysis')
  except Exception, e:
    click.echo('Failed to create analysis. Please check the YAML file format')

@cli.command(name = 'add-request')
@click.argument('data')
def add_request(data):
  
  read_config()
  if not os.path.isfile(data):
    click.echo('File does not exit!')
    return

  f = open(data)
  data_map = yaml.load(f)
  f.close()
  
  try:
    recastapi.request.create(analysis_id=data_map['analysis_id'],
                             description_model=data_map['description_model'],
                             reason_for_request=data_map['reason_for_request'],
                             additional_information=data_map['additional_information'],
                             status=data_map['status'],
                             file_path=data_map['file_path'],
                             parameter_value=data_map['parameter_value'],
                             parameter_title=data_map['parameter_title']
                             )
    click.echo('Successfully created the request')
  except Exception, e:
    click.echo('Failed to create the request. Please check the YAML file format')
                            
@cli.command(name= 'download-basic-request')
@click.option('--path', help='Enter download destination')
@click.argument('request_id')
@click.argument('point_request_index')
@click.argument('basic_request_index')
def download_basic_request(request_id, point_request_index, basic_request_index, path):

  click.echo(basic_request_index)
  click.echo(path)
  recastapi.request.download(int(request_id),
                             int(point_request_index),
                             int(basic_request_index),
                             path)

@cli.command(name = 'upload-basic-request')
@click.option('--request_id', help='Request ID')
@click.option('--basic_id', help='Basic Request ID')
@click.option('--path', help='File to upload')
def upload_basic_request(request_id, basic_id, path):
  read_config()
  recastapi.request.upload_file(request_id=request_id,
                                basic_request_id=basic_id,
                                filename=path)

@cli.command(name = 'download-basic-response')
@click.option('--path', help='Enter download destination')
@click.argument('response_id')
@click.argument('point_response_index')
@click.argument('basic_response_index')
def download_basic_response(response_id, point_response_index, basic_response_index, path):
  
  click.echo(path)
  recastapi.response.download(int(response_id),
                              int(basic_response_index),
                              int(basic_response_index),
                              path)

@cli.command(name = 'upload-basic-response')
@click.option('--basic_id', help='Basic Request')
@click.option('--path', help='File to upload')
def upload_basic_response(basic_id, path):
  read_config()
  recastapi.response.upload_file(basic_response_id=basic_id,
                                 file_name=path)
  
@cli.command(name = 'request-tree')
@click.argument('request_id')
def request_tree(request_id):
  recastapi.request.request_tree(request_id)

@cli.command(name = 'response-tree')
@click.argument('response_id')
def response_tree(response_id):
  recastapi.request.response_tree(response_id)

def read_config(config_file=None):
  default_config = 'recastcli/resources/config.yaml'
  config_file = config_file or default_config

  f = open(config_file)
  config = yaml.load(f)
  f.close()

  recastapi.ORCID_ID = config['ORCID_ID']
  recastapi.ACCESS_TOKEN = config['ACCESS_TOKEN']
