import firebase
import os

class SimpleFirebaseManager:
    def __init__(self, config, url_expiration_hour=100000):
        self.app = firebase.initialize_app(config)
        self.storage = self.app.storage()
        self.url_expiration_hour = url_expiration_hour

    def upload_file(self, file_path: str, storage_path: str):
        """Uploads a file to Firebase Storage at the specified storage path."""
        self.storage.child(storage_path).put(file_path)
        return self.storage.child(storage_path).get_url(expiration_hour=self.url_expiration_hour)

    def get_url_for_file(self, storage_path: str):
        """Gets the URL for a file in Firebase Storage at the specified storage path."""
        return self.storage.child(storage_path).get_url(expiration_hour=self.url_expiration_hour)
    
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
    
    def delete_a_file(self, storage_path):
        """Deletes a file from Firebase Storage from the specified storage path."""
        return self.storage.child(storage_path).delete()

    def list_all_files(self):
        """Lists all files in Firebase Storage."""
        iterator = self.storage.list_files()
        # use list comprehension to get all the files
        list_of_files = [file.name for file in iterator]
        return list_of_files