from flask import Flask, request
import os
app = Flask(__name__)
# Patrick Elser pte6144@rit.edu


@app.route("/", methods=["POST"])
def process():
    """
    Processes a post request by creating a file in the data directory with the supplied contents
    :return: A message to create an HTTP 200 reply
    """
    dictionary = request.form.to_dict()
    for filepath in dictionary:
        paths = filepath.split("\\")
        for i in range(len(paths)):
            if not os.path.exists("data\\" + "\\".join(paths[:i])):
                os.mkdir("data\\" + "\\".join(paths[:i]))
        with open("data\\" + filepath, 'w') as fd:
            fd.write(dictionary[filepath])
        print("Processing " + filepath)
    return "Success"


if __name__ == "__main__":
    app.run(debug=True)

