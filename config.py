login = "solr"
password = "SolrRocks"
host = "localhost"
port = "8983"
name_collection = "new"

flask_port = 5000
auth = (login, password)

url = "http://" + host + ":" + port + "/solr/" + name_collection

# base folder
home_dir = "/"