# models/__init__.py

from.engine.file_storage import FileStorage

# Create a unique FileStorage instance for your application
storage = FileStorage()

# Call the reload method on the storage instance
storage.reload()