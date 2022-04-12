from flask import Flask, render_template, redirect, url_for,request
from flask import make_response
from flask import jsonify
from flask import send_file
import json
app = Flask(__name__)
import createImages as ci


@app.route('/generator/<count>', methods=['GET', 'POST'])
def generator(count):
    main_address = "/home/maryam/Documents/vscode/NFT-Generator-Python/images"
    jsonn = ci.nftGenerator(main_address, int(count))
    
    response = jsonify({'items': jsonn})

    with open(main_address + '/jsonResults.json', 'w') as f:
        f.write(json.dumps({'items': jsonn}, sort_keys = True, ensure_ascii=False))


    # Enable Access-Control-Allow-Origin
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route('/get-nftresults', methods=['GET', 'POST'])
def getNFTResults():
    main_address = "/home/maryam/Documents/vscode/NFT-Generator-Python/images"
    
    with open(main_address + '/jsonResults.json') as json_data:
        data = json.load(json_data)
    
    response = jsonify(data)
    
    print(type(data))
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route("/imgs/<imageName>")
def images(imageName):
    filename = "//home//maryam//Documents//vscode//NFT-Generator-Python//images//results//" + imageName + ".png"
    return send_file(filename, mimetype='image/png')

if __name__ == "__main__":
    app.run(debug = True)

