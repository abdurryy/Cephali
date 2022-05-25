from flask import Flask, render_template, jsonify
from captcha import Cephali

app = Flask(__name__,static_url_path='/assets/website_assets', template_folder='assets/website_pages', static_folder='assets/website_assets')

@app.route("/api/captcha/solve/<site_key>")
def solve_captcha(site_key):
    return render_template("captcha.html", site_key=site_key)

@app.route("/api/captcha/solve/start-selenium/<site_key>", methods=["GET"])
def start_selenium(site_key):
    return jsonify(response_token=Cephali.solve(site_key))

app.run(debug=True, port=5000, host="localhost")