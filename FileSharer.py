from filestack import Client
class FileSharer:
    def __init__(self, filepath, api_key="AsqXD6Y1OTleolBrI9jeMz"):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url