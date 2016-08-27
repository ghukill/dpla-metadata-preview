# console work
from django.conf import settings
from oai.models import Server, Identifier, Record

server = Server()
test_records = [ server.get_record(ident) for ident in settings.TEST_IDENTIFIERS ]

cfai_example = test_records[0]