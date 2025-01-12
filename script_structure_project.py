import os


def create_project_structure(base_path):
    # Define the structure as a dictionary
    structure = {
        "src": {
            "__init__.py": "",
            "main.py": "",
            "modules": {
                "__init__.py": "",
                "funciones.py": "",
                "utils.py": "",
                "auth": {
                    "__init__.py": "",
                    "login.py": "",
                    "register.py": "",
                },
                "api": {
                    "__init__.py": "",
                    "api_client.py": "",
                    "endpoints.py": "",
                },
                "data": {
                    "__init__.py": "",
                    "database.py": "",
                    "models.py": "",
                },
            },
            "services": {
                "__init__.py": "",
                "user_service.py": "",
                "post_service.py": "",
                "notification_service.py": "",
            },
            "config": {
                "__init__.py": "",
                "settings.py": "",
                "secrets.py": "",
            },
        },
        "tests": {
            "__init__.py": "",
            "test_main.py": "",
            "test_auth.py": "",
            "test_api.py": "",
            "test_services.py": "",
        },
        "docs": {
            "README.md": "# Documentation\n",
            "API.md": "# API Documentation\n",
        },
        "scripts": {
            "deploy.sh": "#!/bin/bash\necho 'Deploy script'\n",
            "setup.sh": "#!/bin/bash\necho 'Setup script'\n",
            "backup.py": "# Backup script\n",
        },
        "static": {
            "css": {},
            "js": {},
            "img": {},
        },
        ".env": "",
        "requirements.txt": "",
        "pyproject.toml": "",
        "Makefile": "",
        "README.md": "# Project Documentation\n",
    }

    def create_files_and_dirs(path, structure):
        for name, content in structure.items():
            current_path = os.path.join(path, name)
            if isinstance(content, dict):
                os.makedirs(current_path, exist_ok=True)
                create_files_and_dirs(current_path, content)
            else:
                with open(current_path, "w") as file:
                    file.write(content)

    # Start creating the structure
    create_files_and_dirs(base_path, structure)


# Usage
base_path = "."
os.makedirs(base_path, exist_ok=True)
create_project_structure(base_path)
print(f"Project structure created under {base_path}/")
