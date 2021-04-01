import requests
import json


# Opens config file that stores Moz Links API credentials
with open("../config.json") as CONFIG:
    CONFIG = json.load(CONFIG)

    
# reads config.json for links API access_id and secret_key
access_id = CONFIG["links_api"]["access_id"]
secret_key = CONFIG["links_api"]["secret_key"]


# https://moz.com/help/links-api/making-calls/anchor-text
def anchor_text(access_id, secret_key):
    auth = (access_id, secret_key)
    url = 'https://lsapi.seomoz.com/v2/anchor_text'
    data = """{
                    "target": "moz.com/blog",
                    "scope": "page",
                    "limit": 1
               }"""
    request = requests.post(url, data=data, auth=auth)

    return request


# https://moz.com/help/links-api/making-calls/final-redirect
def final_redirect(access_id, secret_key):
    auth = (access_id, secret_key)
    url = 'https://lsapi.seomoz.com/v2/final_redirect'
    data = """{
                    "page": "seomoz.org/blog"
               }"""
    request = requests.post(url, data=data, auth=auth)

    return request


# https://moz.com/help/links-api/making-calls/global-top-pages
def global_top_pages(access_id, secret_key):
    auth = (access_id, secret_key)
    url = 'https://lsapi.seomoz.com/v2/global_top_pages'
    data = """{
                    "limit": 1
               }"""
    request = requests.post(url, data=data, auth=auth)

    return request

# https://moz.com/help/links-api/making-calls/global-top-root-domains
def global_top_root_domains(access_id, secret_key):
    auth = (access_id, secret_key)
    url = 'https://lsapi.seomoz.com/v2/global_top_root_domains'
    data = """{
                    "limit": 1
                }"""
    request = requests.post(url, data=data, auth=auth)

    return request


# https://moz.com/help/links-api/making-calls/index-metadata
def index_metadata(access_id, secret_key):
    auth = (access_id, secret_key)
    url = 'https://lsapi.seomoz.com/v2/index_metadata'
    data = "{}"
    request = requests.post(url, data=data, auth=auth)

    return request


# https://moz.com/help/links-api/making-calls/link-intersect
def link_intersect(access_id, secret_key):
    auth = (access_id, secret_key)
    url = 'https://lsapi.seomoz.com/v2/link_intersect'
    data = """{
                    "positive_targets": [{
                                            "target": "latimes.com",
                                            "scope": "root_domain"
                                        },
                                        {
                                             "target": "blog.nytimes.com",
                                             "scope":"subdomain"
                                        }],
                    "negative_targets": [{
                                            "target": "moz.com",
                                            "scope": "root_domain"
                                        }],
                    "source_scope": "page",
                    "sort": "source_domain_authority",
                    "limit": 1
                }"""
    request = requests.post(url, data=data, auth=auth)

    return request


# https://moz.com/help/links-api/making-calls/link-status
def link_status(access_id, secret_key):
    auth = (access_id, secret_key)
    url = 'https://lsapi.seomoz.com/v2/link_status'
    data = """{
                    "target": "moz.com/blog",
                    "sources": ["twitter.com", "linkedin.com"],
                    "source_scope": "root_domain",
                    "target_scope": "page"
                }"""
    request = requests.post(url, data=data, auth=auth)

    return request


# https://moz.com/help/links-api/making-calls/linking-root-domains
def linking_root_domains(access_id, secret_key):
    auth = (access_id, secret_key)
    url = 'https://lsapi.seomoz.com/v2/linking_root_domains'
    data = """{
                    "target": "moz.com/blog",
                    "target_scope": "page",
                    "filter": "external",
                    "sort": "source_domain_authority",
                    "limit": 1
                }"""
    request = requests.post(url, data=data, auth=auth)

    return request    


# https://moz.com/help/links-api/making-calls/links
def links(access_id, secret_key):
    auth = (access_id, secret_key)
    url = 'https://lsapi.seomoz.com/v2/links'
    data = """{
                    "target": "moz.com/blog",
                    "target_scope": "page",
                    "filter": "external+nofollow",
                    "limit": 1
                }"""
    request = requests.post(url, data=data, auth=auth)

    return request


# https://moz.com/help/links-api/making-calls/top-pages
def top_pages(access_id, secret_key):
    auth = (access_id, secret_key)
    url = 'https://lsapi.seomoz.com/v2/top_pages'
    data = """{
                    "target": "moz.com",
                    "scope": "root_domain",
                    "limit": 1
                }"""
    request = requests.post(url, data=data, auth=auth)

    return request


# https://moz.com/help/links-api/making-calls/url-metrics
def url_metrics(access_id, secret_key):
    auth = (access_id, secret_key)
    url = 'https://lsapi.seomoz.com/v2/url_metrics'
    data = '{"targets": ["moz.com", "google.com"]}'
    request = requests.post(url, data=data, auth=auth)

    return request


# https://moz.com/help/links-api/making-calls/usage-data
def usage_data(access_id, secret_key):
    auth = (access_id, secret_key)
    url = 'https://lsapi.seomoz.com/v2/usage_data'
    data = "{}"
    request = requests.post(url, data=data, auth=auth)

    return request


# retrieve the data (example with anchor_text)
response_json = anchor_text(access_id, secret_key).json()
print(response_json)
