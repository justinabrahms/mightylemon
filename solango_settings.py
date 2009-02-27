# SOLANGO SETTINGS
### Search-specific settings.
SEARCH_UPDATE_URL = "http://localhost:8983/solr/update"
SEARCH_SELECT_URL = "http://localhost:8983/solr/select"
SEARCH_PING_URLS = ["http://localhost:8983/solr/admin/ping",]

#### SOLR
SOLR_ROOT = '/Users/jlilly/Desktop/apache-solr-1.3.0/example/'
SOLR_SCHEMA_PATH = SOLR_ROOT + 'solr/conf/schema.xml'
SOLR_DATA_DIR = SOLR_ROOT + 'solr/data'

### Default Sorting criteria
SEARCH_SORT_PARAMS = {
        # "field direction": "anchor" The anchor for display purposes
        "score desc": "Relevance",
        "date desc": "Date"
}

### Default Facet Settings
SEARCH_FACET_PARAMS = [
    ("facet", "true"),             # Basic faceting
    ("facet.field", "model"),      # Facet by model
]

SEARCH_HL_PARAMS = [
    ("hl", "true"),      # basic highlighting
    ("hl.fl", "text"),   # What field to highlight
]

# Lucene Special Characters
# + - && || ! ( ) { } [ ] ^ " ~ * ? : \
SEARCH_SEPARATOR = "__"

FACET_SEPARATOR = ";;"

########## LOGGING ##############

# The filename to which the logger will write.
import os
DIRNAME = os.path.abspath(os.path.dirname(__file__))
LOG_FILENAME = DIRNAME + "solango.log"

# The log level: DEBUG, INFO, WARNING, ERROR, CRITICAL.
LOG_LEVEL =  "DEBUG"

# The log message format.
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s - %(filename)s:%(funcName)s:%(lineno)d"
