from flask import Flask, render_template, request, jsonify
import aiml
import glob
import os

app = Flask(__name__)
kernel = aiml.Kernel()

# Загрузка AIML-файлов с обработкой ошибок
for aiml_file in glob.glob("botlibre/*.aiml"):
    try:
        kernel.learn(aiml_file)
        print(f"Loaded: {os.path.basename(aiml_file)}")
    except Exception as e:
        print(f"Error in {os.path.basename(aiml_file)}: {str(e)}")

@app.route("/")
def home():
    return render_template("html.html")  # Теперь используется относительный путь

@app.route("/get_response", methods=["POST"])
def get_response():
    user_message = request.json.get("message", "")
    bot_response = kernel.respond(user_message)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)