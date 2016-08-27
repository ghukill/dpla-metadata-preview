
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
		sickle_record = self.sickle_api.GetRecord(identifier=identifier, metadataPrefix=metadataPrefix)
		return Record(identifier, sickle_record)


class Identifier(object):

	'''
	Wrapper for identifier response
	'''

	def __init__(self, record_headers):
		self.datestamp = record_headers.datestamp
		self.deleted = record_headers.deleted
		self.identifier = record_headers.identifier
		self.raw= record_headers.raw
		self.setSpecs = record_headers.setSpecs
		self.xml = record_headers.xml


class Record(object):
	
	'''
	wrapper for Sickle Record
	'''

	def __init__(self, identifier, sickle_record):
		self.identifier = identifier
		self.sickle_api = sickle_record

		# read XML, derive common values
		self.metadata = self.sickle_api.xml.find('{http://www.openarchives.org/OAI/2.0/}metadata')
		self.title = self.sickle_api.metadata['title'][0]
		self.thumbnail_url = self.metadata.xpath('//mods:url[@access="preview"]', namespaces={'mods':'http://www.loc.gov/mods/v3'})[0].text

	def __repr__(self):
		return "<dplamp.oai.Record: %s / %s>" % (self.title, self.identifier)

	def __str__(self):
		return "<dplamp.oai.Record: %s / %s>" % (self.title, self.identifier)


class Set(object):

	pass