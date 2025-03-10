"""An example config.py file."""

import ee

# The service account email address authorized by your Google contact.
# Set up a service account as described in the README.
EE_ACCOUNT = 'sowelhaz@webapp644378.iam.gserviceaccount.com'

# The private key associated with your service account in JSON format.
EE_PRIVATE_KEY_FILE = 'data/ee_config/clé_EarthEngine.json'

EE_CREDENTIALS = ee.ServiceAccountCredentials(EE_ACCOUNT, EE_PRIVATE_KEY_FILE)
# print('oui')