from flask import Flask, request, render_template
from links_to_screenshot import links_to_screenshot
from gemeni_UI_score import score
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/get-score/')
def get_text():
    link = request.args.get('link')  # Get the value of the 'link' parameter
    links_to_screenshot(link)
    print("Screenshot taken...")

    Sc=score('screenshot.png')
    print("Score calculated...")
    return Sc
if __name__ == '__main__':
    app.run(debug=True)
