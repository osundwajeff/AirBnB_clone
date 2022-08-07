#!/usr/bin/python3
"""_init_ magic method for models directory,
to create a unique FileStorage instance for your application
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
