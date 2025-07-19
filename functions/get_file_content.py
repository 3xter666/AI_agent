import os 
from functions import config
from  google.genai import types
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Retrieves the content of a specific file within the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to read, relative to the working directory. If not provided, reads from the working directory itself.",
            ),
        },
    ),
)
def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    # This check ensures abs_file_path is inside abs_working_dir
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        with open(abs_file_path, 'r') as file:
            content = file.read(config.MAX_FILE_SIZE + 1)
            if len(content) > config.MAX_FILE_SIZE:
                content = content[:config.MAX_FILE_SIZE] + f"[...File \"{file_path}\" truncated at {config.MAX_FILE_SIZE} characters]"
        return content
    except Exception as e:
        return f"Error: {str(e)}"