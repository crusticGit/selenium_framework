import os
import random
import tempfile

from faker import Faker

from logger.logger import Logger


class FileUtilities:
    @staticmethod
    def create_temp_file(content: str = None, suffix: str = None) -> str:
        if suffix is None:
            formats = ['.txt', '.html', '.json', '.csv', '.docx']
            suffix = random.choice(formats)

        with tempfile.NamedTemporaryFile(mode='w', suffix=suffix, delete=False) as temp_file:
            Logger.info(f"Create tempfile for test : {temp_file}")
            temp_file.write(Faker().text() if content is None else content)
        return temp_file.name

    @staticmethod
    def delete_file(file_path: str) -> None:
        if os.path.exists(file_path):
            Logger.info(f"Delete tempfile: {file_path}")
            os.unlink(file_path)
