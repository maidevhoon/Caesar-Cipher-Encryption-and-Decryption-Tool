from flask import Flask, render_template, request

app = Flask(__name__)

def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        message = request.form.get("message")
        shift = int(request.form.get("shift"))
        action = request.form.get("action")
        
        if action == "encrypt":
            result = caesar_cipher(message, shift)
        elif action == "decrypt":
            result = caesar_cipher(message, -shift)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
