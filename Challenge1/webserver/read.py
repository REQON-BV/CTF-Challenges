import zipfile
import re
import hashlib
from flask import Flask, flash, request, redirect, render_template, url_for
from werkzeug.utils import secure_filename
from lxml import etree


app = Flask(__name__)


def isdir(z, name):
    return any(x.startswith("%s/" % name.rstrip("/")) for x in z.namelist())


def parse_xml(file):
    data = {}
    parser = etree.XMLParser(no_network=False, load_dtd=True,
                             recover=True, resolve_entities=True, huge_tree=True)
    tree = etree.parse(file, parser)
    root = tree.getroot()

    for child in root:
        # Remove all between {} to print out nice tags
        child.tag = re.sub('{[^}]+}', '', child.tag)
        if child.text != None:
            hash_object = hashlib.sha1(child.text.encode())
            hex_dig = hash_object.hexdigest()
            data[child.tag] = str(hex_dig)
    return data


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/process_file', methods=['GET', 'POST'])
def process_file():
    if request.method == 'POST':
        file = request.files.get('file')
        if file:
            try:
                with zipfile.ZipFile(file) as zip_ref:
                    if not isdir(zip_ref, 'xl') or not isdir(zip_ref, 'docProps'):
                        raise "Not valid"
                    output = parse_xml(zip_ref.open('docProps/core.xml'))
                    print(output)
            except Exception:
                message = "<div class='alert-danger'>Not a valid Microsoft Office Excel file</div>"
                return render_template('home.html', message=message)

            message = "<div class='alert-success'>File procesed succesfull </div>"
            return render_template('home.html', message=message, output=output)
        else:
            message = "<div class='alert-danger'>No file selected for submission!</div>"
            return render_template('home.html', message=message)
    else:
        return render_template('home.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0")
