from flask import Flask

# first create the app 
app= Flask(__name__)

# we are going to create the routes 
@app.route("/") 
def home() :
    sam=input (" enter your name :")
    return " this is what is the best man need for writing the codes for the main " \
    "and finding what other man can not find "

# and then we have to insured that this will run if and only if this files is only the one which has neen 
# run 
if __name__== "__main__":
    app.run (debug=True) 