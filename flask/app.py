import os
from flask import Flask, request, render_template, send_file
#from azure.identity import DefaultAzureCredential
#from azure.storage.queue import QueueServiceClient, QueueClient, QueueMessage
#from queue import Queue

app = Flask(__name__)
#q = Queue(maxsize = 0)

# NEED TO IMPLEMENT QUEUE OPERATIONS

@app.route('/')
def upload_file():
    return render_template('upload.html')


@app.route('/process', methods=['GET', 'POST'])
def process_file():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            # Save the uploaded file to a location (e.g., same directory as app.py)
            uploaded_file.save(uploaded_file.filename)
            
            # Read the contents of the uploaded file
            with open(uploaded_file.filename, 'r') as file:
                content = file.read()
            
            # Model iOS vs iOS XE command swaps for demo app
            iOS_dict = {"1":"one", "2":"2", "3":"three", "4":"4", "5":"five", "6":"6", "7":"seven", "8":"8", "9":"nine", "10":"10"}

            # Manipulate data from input.txt before writing to output.txt
            updated_content = []
            for line in content.splitlines():
                tokens = line.strip().split()  # Split by whitespace
                for token in tokens:
                    if token in iOS_dict:
                        updated_content.append(iOS_dict[token])
                    else:
                        updated_content.append(token)

            # Join the updated content back into lines
            updated_lines = "\n".join(updated_content)

            # Write the contents to an output file (e.g., output.txt)
            with open('output.txt', 'w') as output_file:
                output_file.write(updated_lines) 
            
            return "File uploaded and contents saved to output.txt. <a href='/'>Go back</a>"
        else:
            return "No file uploaded."
    else:
        # Handle GET requests (e.g., display an upload form)
        return render_template('upload.html')
    
@app.route('/download')
def download_file():
    # Specify the path to your output.txt file
    file_path = 'output.txt'
    
    # Check if the file exists
    if os.path.exists(file_path):
        # Use send_file to send the file as an attachment
        return send_file(file_path, as_attachment=True)
    else:
        return "The output file does not exist yet. Please upload a file and process it first. <a href='/'>Go back</a>"


if __name__ == '__main__':
    app.run(debug=True)
