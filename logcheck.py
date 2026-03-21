def check_log():
    """
    Look for error lines in a log
    
    This function asks the user for a logs file name and prints all lines with ERROR status 
    """
    
    log = ""
    
    try:
        file_name = input("Enter a file name\n")
        file_path = f"{f"./{file_name}"}"
        
        with open(file_path, 'r') as log_file:
            log = log_file.read()

    except FileNotFoundError as e:
    print(f"Error: The file '{file_path}' was not found.")
    print(f"An error occurred: {e.strerror}")
        
    log_lines = log.split("\n")
        
    for line in log_lines:
        if "ERROR" in line:
            print("Error:", line)
