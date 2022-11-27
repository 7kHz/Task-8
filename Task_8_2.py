import requests
from Security import TOKEN


class YaUploader:
    Host = 'https://cloud-api.yandex.net/'

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
        'Content-Type': 'application/json',
        'Authorization': f'OAuth {self.token}'
    }

    def upload(self, path):
        uri = 'v1/disk/resources/upload/'
        url = self.Host + uri
        params = {'path': path, 'overwrite': True}
        response = requests.get(url, headers=self.get_headers(), params=params)
        print(response.status_code)
        return response.json()['href']

    def upload_to_disk(self, path_to_file, yandex_path):
        url_upload = self.upload(yandex_path)
        response = requests.put(url_upload, headers=self.get_headers(), data=open(path_to_file, 'rb'))
        return response.status_code

if __name__ == '__main__':
    uploader = YaUploader(TOKEN)
    print(uploader.upload_to_disk('new_file.txt', '/new_file.txt'))
