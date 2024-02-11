import importlib.util
import os

# yeni header'lar buraya
header_files = ["x_content_type_options.py", "x_xss_protection.py"]

HEADER_DIR = os.path.join(os.getcwd(), "headers")

def load_headers():
    headers = {}

    counter = 0


    for file_name in header_files:
        header_name = file_name.split(".")[0]
        module_name = f"{header_name}"
        file_path = os.path.join(HEADER_DIR, file_name)

        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        header_info = module.get_info()
        key = f"key{counter}"
        headers[key] = header_info
        counter += 1
    return headers


def main():
    headers = load_headers()
    
    for i in range(len(headers)):
        print(headers[f"key{i}"]['description'])

    

if __name__ == "__main__":
    main()
