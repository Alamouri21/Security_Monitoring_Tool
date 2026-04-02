## This tool scans the current directory for `.log` files and checks their sizes.
## It uses the `os` library to list files and determine their sizes, labeling them as 'SMALL' or 'LARGE'.

def log_file_scanner():
    import os
    log_files = [f for f in os.listdir('.') if f.endswith('.log')]  
    
    for file in log_files: 
        file_size = os.stat(file).st_size
        file_size_mb = file_size / (1024 * 1024)  
        
        
        size_label = 'LARGE' if file_size_mb >= 1 else 'SMALL'
        
        
        print(f"File: {file}, Size: {file_size_mb:.2f} MB, Label: {size_label}")
        
if __name__ == "__main__":
    log_file_scanner()