# console



# load test record with oai module
from oai import models as oai_models
s = oai_models.Server()
r = s.get_record(oai_models.settings.TEST_IDENTIFIERS[0])


