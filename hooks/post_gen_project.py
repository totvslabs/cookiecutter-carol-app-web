#!/usr/bin/env python
import http.client
import os
import platform
import urllib.parse

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))

def post_ga_data():
    params = urllib.parse.urlencode({
        'v': 1,
        'tid': 'UA-144583662-1',
        'uid': '{{ cookiecutter.user_email }}',
        't' : 'event',
        'ec': 'carol_cookiecuter',
        'ea': 'new_web_project',
        'el': 'carol_web_app',
        'cd1': 'organization',
        'cm1': '{{ cookiecutter.carol_app_organization }}',
        'cd2': 'environment',
        'cm2': '{{ cookiecutter.carol_app_environment }}',
        'cd3': 'project',
        'cm3': '{{ cookiecutter.project_name }}',
        'cd4': 'os',
        'cm4': platform.system(),
    })

    try:
        connection = http.client.HTTPConnection('www.google-analytics.com')
        connection.request('POST', '/collect', params)
    except Exception as e:
        print(e)

post_ga_data()

print("{{ cookiecutter.project_name }} created successfully.")

if __name__ == '__main__':
    pass
