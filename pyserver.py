from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import threading
from termcolor import colored  # Importing termcolor for colored output

# Flag to indicate if the server should exit
exit_server = False

class CustomRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        # Specify the path where you want to save the uploaded file
        file_path = "uploaded_file.txt"  # Change this to your desired file path

        # Save the uploaded data to the specified file
        with open(file_path, 'wb') as file:
            file.write(post_data)

        # Send a success response
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Success! File Accepted!')

        # Print success message
        print(colored("Success! File Accepted!", 'green'))

def start_server(port):
    server_address = ('', port)
    httpd = HTTPServer(server_address, CustomRequestHandler)
    
    # Print the HTTP SERVER ASCII art banner
    banner = """
╦ ╦╔╦╗╔╦╗╔═╗   ╔═╗╔═╗╦═╗╦  ╦╔═╗╦═╗
╠═╣ ║  ║ ╠═╝───╚═╗║╣ ╠╦╝╚╗╔╝║╣ ╠╦╝
╩ ╩ ╩  ╩ ╩     ╚═╝╚═╝╩╚═ ╚╝ ╚═╝╩╚═
            -SCARIO-
    """
    print(colored(banner, 'green'))
    print(f"Server started on port {port}...")
    httpd.serve_forever()

def run():
    global exit_server
    try:
        port = int(input(colored("Enter the port number to run the server on: ", 'red')))
        thread = threading.Thread(target=start_server, args=(port,))
        thread.start()
        thread.join()  # Wait for the server thread to finish
    except ValueError:
        print("Invalid port number. Please enter a valid port number.")
    except OSError as e:
        if e.errno == 98:
            print("Port is already in use. Choose a different port.")
        else:
            print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nServer is shutting down...")
        exit_server = True

if __name__ == '__main__':
    run()
