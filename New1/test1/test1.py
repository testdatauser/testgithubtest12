from flask import Flask, Response
import json
import urllib
import base64

app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Hello, World!"

# @app.route("/")
# def attachment():
#     url='https://raw.githubusercontent.com/testdatauser/test_githubrepo1/master/README.md'

#     file_name = url.split('/')[-1]
#     print(file_name)

#     # Download the file from `url` and save it locally under `file_name`:
#     with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
#         shutil.copyfileobj(response, out_file)

#     # resp = make_response('my text file')
#     # print(resp)
#     resp.headers['Content-Type'] = 'text/plain;charset=UTF-8'
#     resp.headers['Content-Disposition'] = 'attachment;filename={file_name}'
#     return resp

# @app.route("/")
# def attachment():
#     url='https://raw.githubusercontent.com/testdatauser/test_githubrepo1/master/README.md'

#     file_name = url.split('/')[-1]
#     print(file_name)

#     file_data = "dGVzdGluZyAxMDE=\n"
#     # Download the file from `url` and save it locally under `file_name`:
#     response = make_response(file_data)
#     response['Content-Disposition'] = 'attachment; filename="README12.md"'
#     return response

# @app.route("/")
# def attachment():
#     file_data = "dGVzdGluZyAxMDE=\n"
#     # Download the file from `url` and save it locally under `file_name`:
#     response = make_response(file_data)
#     response.headers['Content-Type'] = 'text/plain;charset=base64'
#     response.headers['Content-Disposition'] = 'attachment;filename=README12.md'
#     return response

@app.route("/")
def attachment():
    file_name = "hello.txt"
    print(file_name)
    response = "dGVzdGluZyAxMDE=\n"
    mystr_decoded = base64.b64decode(response).decode('UTF-8')
    print(mystr_decoded)
    return Response(mystr_decoded, status=200,
                    headers={"Content-Disposition": f"attachment;filename={file_name}"})

    
if __name__ == "__main__":
    app.run(debug=True)