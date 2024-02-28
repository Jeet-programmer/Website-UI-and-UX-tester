import google.generativeai as genai
from IPython.display import Markdown
import textwrap
import PIL.Image
import ast

genai.configure(api_key="AIzaSyBGHWnbEC6sDR0BNfWdmMRDcBZeiemdeAg")
def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

def score(image):
    img = PIL.Image.open(image)

    print("Generating score...")
    model = genai.GenerativeModel('gemini-pro-vision')

    response = model.generate_content(["Give a score from 0 to 10 on the UI and UX of the screenshot of the website also suggest some changes or suggestions to improve it better give give a detalied remarks and suggesion it in a format of json {'UI': 'score', 'UI_remark': 'remark', 'UX': 'score', 'UX_remark': 'remark', 'UI_suggestions': 'suggestions', 'UX_suggestions': 'suggestions'}", img], stream=True)
    response.resolve()
    A=response.text
    A= A.strip('```').strip()
    A = A.strip('```json').strip()

    # print(A)
    # Convert the string to a dictionary
    A_dict = ast.literal_eval(A)
    print("A_dict", A_dict)
    return A_dict
    
# print(score("screenshot.png"))