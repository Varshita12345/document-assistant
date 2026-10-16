import os

def read_document(filename: str) -> str:
    """
    Safely opens and reads the text content from a specified document file.
    
    Args:
        filename (str): The name or path of the file to read.
        
    Returns:
        str: The raw text content of the file, or an empty string if reading fails.
    """
    # Clean up any accidental spacing in the filename input
    cleaned_filename = filename.strip()
    
    # Check if the file exists on the system path before attempting to open it
    if not os.path.exists(cleaned_filename):
        print(f"[Tools Error]: The file '{cleaned_filename}' could not be located.")
        return ""
        
    try:
        # Open with utf-8 encoding to support various characters seamlessly
        with open(cleaned_filename, 'r', encoding='utf-8') as file:
            content = file.read()
            return content
            
    except UnicodeDecodeError:
        # Fallback to default system encoding if utf-8 fails
        try:
            with open(cleaned_filename, 'r', encoding='errors-replace') as file:
                return file.read()
        except Exception as e:
            print(f"[Tools Error]: Failed to parse encoding. Details: {str(e)}")
            return ""
            
    except Exception as e:
        print(f"[Tools Error]: An unexpected error occurred while reading the file: {str(e)}")
        return ""
