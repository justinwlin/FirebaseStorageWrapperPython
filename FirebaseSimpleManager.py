import firebase

class SimpleFirebaseManager:
    def __init__(self, config):
        self.app = firebase.initialize_app(config)
        self.storage = self.app.storage()

    def upload_file(self, file_path: str, storage_path: str):
        """Uploads a file to Firebase Storage at the specified storage path."""
        self.storage.child(storage_path).put(file_path)

    def download_file(self, storage_path: str, download_path: str):
        """Downloads a file from Firebase Storage from the specified storage path."""
        try:
            self.storage.child(storage_path).download(download_path)
            if not os.path.exists(download_path):
                raise FileNotFoundError(f"Failed to download the file: {download_path}")
            else:
                print(f"File downloaded successfully: {download_path}")
        except Exception as e:
            print(f"An error occurred: {e}")
    
    def list_all_files(self):
        """Lists all files in Firebase Storage."""
        iterator = self.storage.list_files()
        # use list comprehension to get all the files
        list_of_files = [file.name for file in iterator]
        return list_of_files