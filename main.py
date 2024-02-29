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
    if link == "test":
        return {'UI': 7, 'UI_remark': 'The UI is clean and modern, but it could be more user-friendly. The font is a bit difficult to read, and the colors are a bit too bright.', 'UX': 6, 'UX_remark': 'The UX is good, but it could be improved. The navigation is a bit confusing, and the search bar is not very prominent.', 'UI_suggestions': 'Use a more readable font. Use a more muted color scheme. Make the search bar more prominent.', 'UX_suggestions': 'Simplify the navigation. Make the search bar more prominent.'}
    links_to_screenshot(link)
    print("Screenshot taken...")

    Sc=score('screenshot.png')
    print("Score calculated...")
    return Sc
if __name__ == '__main__':
    app.run(debug=True)
