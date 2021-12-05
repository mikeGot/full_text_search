import os
import requests


class Solr:
    def __init__(self, ip, port, collection="", login="", password=""):
        self.ip = ip
        self.port = port
        self.url = "http://" + str(ip) + ":" + str(port) + "/solr/" + collection
        # self.url = "http://" + str(ip) + ":" + str(port)
        self.login = login
        self.password = password
        self.collection = collection

        print(self.url)

        # TODO

    def check_health(self):
        core_overview = self.url + "/core-overview"
        print(core_overview)
        req = requests.get(core_overview, auth=(self.login, self.password)).status_code
        if req == 200:
            return True
        else:
            return False

    @staticmethod
    def _parse_response(_response: dict) -> list:
        response_dict_to_list = _response['response']['doc']
        return [r['id'] for r in response_dict_to_list]

    def search(self, query_string=":", rows=10, query_operator="OR", with_parse_response_check_path=True):
        url = self.url + "/query?q=" + query_string + "&q.op=" + query_operator + "&rows=" + str(rows)
        req = requests.get(url, auth=(self.login, self.password))
        if with_parse_response_check_path:
            valid_path, invalid_path = check_path(self._parse_response(req.json()))
            return valid_path, invalid_path
        else:
            return req.json()


def check_path(path_list: list):
    _valid_path = []
    _invalid_path = []

    for path in path_list:
        if os.path.isfile(path):
            _valid_path.append(path)
        else:
            _invalid_path.append(path)
    return _valid_path, _invalid_path


if __name__ == "__main__":
    s = Solr(ip="127.0.0.1", port=8983, collection="films")
    print(s.check_health())
    # s.search("*Thri*", with_parse_response_check_path=False)
    print(s.search("*Thri*", with_parse_response_check_path=False))


