import functions
from google.genai import types
available_functions = types.Tool(
    function_declarations=[
        functions.schema_get_files_info,
        functions.schema_get_file_content,
        functions.schema_run_python_file,
        functions.schema_write_file,
    ]
)