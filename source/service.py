from flask import Flask, render_template, redirect, url_for,request
from flask import make_response
from flask import jsonify
app = Flask(__name__)
import createImages as ci


@app.route('/generator/<count>', methods=['GET', 'POST'])
def generator(count):
    main_address = "/home/maryam/Documents/vscode/NFT-Generator-Python/images"
    jsonn = ci.nftGenerator(main_address, int(count))
    
    response = jsonify({'items': jsonn})

    # Enable Access-Control-Allow-Origin
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

if __name__ == "__main__":
    app.run(debug = True)

