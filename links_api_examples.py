import requests
import json

with open("../../config.json") as CONFIG:
    CONFIG = json.load(CONFIG)


access_id = CONFIG["links_api"]["access_id"]
secret_key = CONFIG["links_api"]["secret_key"]


def anchor_text(access_id, secret_key):
    auth = (access_id, secret_key)
    url = 'https://lsapi.seomoz.com/v2/anchor_text'
    payload = """{
                    "target": "moz.com/blog",
                    "scope": "page",
                    "limit": 1
                }"""
    request = requests.post(url, data=payload, auth=auth)

    return request


def final_redirect(access_id, secret_key):
    auth = (access_id, secret_key)
    url = 'https://lsapi.seomoz.com/v2/final_redirect'
    payload = """{
                    "page": "seomoz.org/blog"
                }"""
    request = requests.post(url, data=payload, auth=auth)

    return request


def global_top_pages(access_id, secret_key):
    auth = (access_id, secret_key)
    url = 'https://lsapi.seomoz.com/v2/global_top_pages'
    payload = """{
                    "limit": 1
                }"""
    request = requests.post(url, data=payload, auth=auth)

    return request


def global_top_root_domains(access_id, secret_key):
    auth = (access_id, secret_key)
    url = 'https://lsapi.seomoz.com/v2/global_top_root_domains'
    payload = """{
                    "limit": 1
                }"""
    request = requests.post(url, data=payload, auth=auth)

    return request


def index_metadata(access_id, secret_key):
    auth = (access_id, secret_key)
    url = 'https://lsapi.seomoz.com/v2/index_metadata'
    payload = "{}"
    request = requests.post(url, data=payload, auth=auth)

    return request


def link_intersect(access_id, secret_key):
    auth = (access_id, secret_key)
    url = 'https://lsapi.seomoz.com/v2/link_intersect'
    payload = """{
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
    request = requests.post(url, data=payload, auth=auth)

    return request


def link_status(access_id, secret_key):
    auth = (access_id, secret_key)
    url = 'https://lsapi.seomoz.com/v2/link_status'
    payload = """{
                    "target": "moz.com/blog",
                    "sources": ["twitter.com", "linkedin.com"],
                    "source_scope": "root_domain",
                    "target_scope": "page"
                }"""
    request = requests.post(url, data=payload, auth=auth)

    return request


def linking_root_domains(access_id, secret_key):
    auth = (access_id, secret_key)
    url = 'https://lsapi.seomoz.com/v2/linking_root_domains'
    payload = """{
                    "target": "moz.com/blog",
                    "target_scope": "page",
                    "filter": "external",
                    "sort": "source_domain_authority",
                    "limit": 1
                }"""
    request = requests.post(url, data=payload, auth=auth)

    return request    


def links(access_id, secret_key):
    auth = (access_id, secret_key)
    url = 'https://lsapi.seomoz.com/v2/links'
    payload = """{
                    "target": "moz.com/blog",
                    "target_scope": "page",
                    "filter": "external+nofollow",
                    "limit": 1
                }"""
    request = requests.post(url, data=payload, auth=auth)

    return request


def top_pages(access_id, secret_key):
    auth = (access_id, secret_key)
    url = 'https://lsapi.seomoz.com/v2/top_pages'
    payload = """{
                    "target": "moz.com",
                    "scope": "root_domain",
                    "limit": 1
                }"""
    request = requests.post(url, data=payload, auth=auth)

    return request


def url_metrics(access_id, secret_key):
    auth = (access_id, secret_key)
    url = 'https://lsapi.seomoz.com/v2/url_metrics'
    payload = '{"targets": ["moz.com", "google.com"]}'
    request = requests.post(url, data=payload, auth=auth)

    return request


def usage_data(access_id, secret_key):
    auth = (access_id, secret_key)
    url = 'https://lsapi.seomoz.com/v2/usage_data'
    payload = "{}"
    request = requests.post(url, data=payload, auth=auth)

    return request
