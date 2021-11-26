import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)


        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.A9CiHzJucfbZDSO1AxlA1mHk9U0l8qRMJPrGauCXwQ-JwmqYvPjhl05_9WaVLEc63bOhp2Vl25j2YEvcngDkwcaKzKrG_KZ-i1IO0TzCpYKj4-BqgoBfplOokjZBSa71vLAfmQVHbj4'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer : -")
    file_to = input("enter the full path to upload to dropbox:- ")  

    
    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")


main()