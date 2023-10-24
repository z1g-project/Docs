import subprocess

def start_mkdocs_serve():
    command = "mkdocs serve -a 0.0.0.0:443"
    subprocess.run(command, shell=True)

# Call the function to start MKDocs server
start_mkdocs_serve()
