from elasticsearch import Elasticsearch

#host = "http://shenvi9.6655.la:26231/" #http://localhost:9200

es = Elasticsearch([{u'host': u'127.0.0.1', u'port': 9200}])
#es = Elasticsearch([{u'host': u'free.ngrok.cc', u'port': 11627}])