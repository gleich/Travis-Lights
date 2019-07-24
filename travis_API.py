import requests
import json

import util


# curl -L http://api.travis-ci.org/repos/goffstown-sports-app/Scrape-Calendar-Data

def get_build_repo_status(repo_id):
    """
    Get the last build for the repo
    :param repo_id: ID for the repo. Example: Matt-Gleich/Photo-Sort
    :return: last_build_status
    """
    # Type Checking:
    util.check_type(repo_id, "str")

    # Querying information
    url = "http://api.travis-ci.org/repos/" + repo_id
    session = requests.Session()
    req = requests.Request("GET", url)
    prepped = session.prepare_request(req)
    resp = session.send(prepped)
    session.close()
    resp_json = json.loads(resp.content.decode("utf-8"))
    print(resp_json)
    return resp_json["last_build_status"]

# Testing:
print(get_build_repo_status("goffstown-sports-app/Scrape-Calendar-Data"))
