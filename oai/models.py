
# django
from django.conf import settings
# django
from django.db import models

# general
import logging
from lxml import etree
import requests

# sickle
from sickle import Sickle
from sickle import models as sickle_models

# project
# from dplamp import settings

# Get an instance of a logger
logger = logging.getLogger(__name__)

# OAI models

class Server(object):

	'''
	wrapper for sickle OAI-PMH serer interface
	'''
	
	def __init__(self):
		self.base_url = settings.OAI_SERVER_BASE_URL
		self.default_set = settings.OAI_SET
		self.default_metadata_prefix = settings.OAI_METADATA_PREFIX

		# init sickle interface
		self.sickle_api = Sickle(self.base_url)


	def get_record(self, identifier, metadataPrefix=settings.OAI_METADATA_PREFIX):
		'''
		todo: add try / except block here
		'''
		response = self.sickle_api.GetRecord(identifier=identifier, metadataPrefix=metadataPrefix)
		return Record(response)


class Record(object):
	
	'''
	wrapper for Sickle Record
	'''

	def __init__(self, record):
		self.sickle_api = record


	def to_string(self):
		return self.record.raw


class Set(object):

	pass