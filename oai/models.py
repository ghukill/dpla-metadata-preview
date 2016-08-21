
# django
from django.conf import settings
from django.db import models

# general
import logging
import requests

# Get an instance of a logger
logger = logging.getLogger(__name__)

# OAI models

class Server(object):
	
	def __init__(self):
		self.base_url = settings.OAI_SERVER_BASE_URL



class Record(object):
	pass