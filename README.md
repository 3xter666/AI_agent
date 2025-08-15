# AI Agent Project

A Python-based AI agent that uses Google's Gemini API to interact with files and execute Python code within a controlled working directory.

## Features

- **File Operations**: Read, write, and list files within a secure working directory
- **Python Execution**: Run Python files safely within the working environment
- **AI-Powered**: Uses Google's Gemini 2.0 Flash model for intelligent task execution
- **Function Calling**: Supports multiple tool functions for file management
- **Security**: Prevents access outside the designated working directory

## Prerequisites

- Python 3.8+
- Google Gemini API key
- `uv` package manager (or pip)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/3xter666/AI_agent
cd AI_agent
```

2. Install dependencies:
```bash
uv sync
```
or with pip:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory:
```bash
GEMINI_API_KEY=your_gemini_api_key_here
```

## Project Structure

```
AI_agent/
├── main.py                    # Main application entry point
├── prompts.py                 # System prompts for the AI agent
├── config.py                  # Configuration settings
├── functions/                 # Function modules
│   ├── __init__.py
│   ├── available_functions.py # Function declarations for Gemini
│   ├── call_function.py       # Function dispatcher
│   ├── get_files_info.py      # List files and directories
│   ├── get_file_content.py    # Read file contents
│   ├── write_file.py          # Write content to files
│   └── run_python_file.py     # Execute Python scripts
├── calculator/                # Test/Working directory for AI operations
└── tests.py                   # Test functions
```

## Usage

Run the AI agent with a prompt:

```bash
uv run main.py "Your prompt here"
```

### Examples

```bash
# List files in the calculator directory
uv run main.py "List all files in the current directory"

# Create a new Python file
uv run main.py "Create a simple calculator program that adds two numbers"

# Read and analyze existing code
uv run main.py "Read the main.py file and explain what it does"

# Run a Python program
uv run main.py "Run the calculator.py file with some test inputs"
```

### Verbose Mode

Add `--verbose` flag for detailed execution information:

```bash
uv run main.py --verbose "Your prompt here"
```

## Available Functions

The AI agent has access to the following functions:

- **`get_files_info`**: Lists files and directories with sizes
- **`get_file_content`**: Reads the content of specified files
- **`write_file`**: Creates or overwrites files with new content
- **`run_python_file`**: Executes Python scripts and returns output

## Security Features

- All file operations are constrained to the `./calculator` working directory
- Path traversal attacks are prevented using absolute path validation
- File size limits are enforced for reading operations
- Error handling prevents system crashes from malformed requests

## Configuration

Edit `config.py` to modify settings:

```python
MAX_FILE_SIZE = 1024 * 1024  # 1MB file size limit
```

## Testing

Run the test suite:

```bash
uv run tests.py
```

## Error Handling

The agent includes comprehensive error handling for:
- Invalid file paths
- Permission errors
- File size limits
- Directory traversal attempts
- API errors and rate limits

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

### Common Issues

1. **ModuleNotFoundError**: Ensure all dependencies are installed with `uv sync`
2. **API Key Error**: Verify your `.env` file contains a valid `GEMINI_API_KEY`
3. **Permission Denied**: Check file permissions in the calculator directory
4. **Max Iterations**: The agent stops after 20 iterations to prevent infinite loops

### Getting Help

- Check the verbose output with `--verbose` flag
- Review error messages for specific issues
- Ensure your Gemini API key has sufficient quota
