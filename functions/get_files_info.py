import os
from google.genai import types
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
def get_files_info(working_directory, directory="."):
    abs_working_dir = os.path.abspath(working_directory)
    abs_target_dir = os.path.abspath(os.path.join(working_directory, directory))
    
    # This check ensures abs_target_dir is inside abs_working_dir
    if not abs_target_dir.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(abs_target_dir):
        return f'Error: "{directory}" is not a directory'
    try:
        res = []
        for i in os.listdir(abs_target_dir):
            filesize = os.path.getsize(os.path.join(abs_target_dir, i))
            is_dir = os.path.isdir(os.path.join(abs_target_dir, i))
            res.append(f"- {i}: file_size={filesize} bytes, is_dir={is_dir}")
        return '\n'.join(res)
    except Exception as e:
        return f"Error: {str(e)}"
