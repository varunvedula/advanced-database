from flask import Flask, render_template, request, redirect, url_for

import database

# remember to $ pip install flask

database.initialize("pets.db")

app = Flask(__name__)

@app.route("/", methods=["GET"]) 
@app.route("/list", methods=["GET"])
def get_list():
    print("in app.py")
    return "List"
    #pets = database.get_pets()
    #return render_template("list.html", pets=pets)     


@app.route("/kind", methods=["GET"])
def get_kind_list():
    print("in kind_list()")
    return "Kind"
    #pets = database.get_pets()
    #return render_template("list.html", pets=pets)


@app.route("/create", methods=["GET"])
def get_create():
    return render_template("create.html")     

@app.route("/create", methods=["POST"])
def post_create():
    data = dict(request.form)
    database.create_pet(data)
    return redirect(url_for("get_list"))  

@app.route("/delete/<id>", methods=["GET"])
def get_delete(id):
    database.delete_pet(id)
    return redirect(url_for("get_list"))  

@app.route("/update/<id>", methods=["GET"])
def get_update(id):
    data = database.get_pet(id)
    return render_template("update.html",data=data)

@app.route("/update/<id>", methods=["POST"])
def post_update(id):
    data = dict(request.form)
    database.update_pet(id, data)
    return redirect(url_for("get_list"))  


# @app.route("/kind", methods=["GET"])
# @app.route("/kind/list", methods=["GET"])
# def get_kind_list():
#     print("in kind list")
#     # kinds = database.get_kinds()
#     kinds = []
#     return "In kind list"
#     return render_template("kind_list.html", kinds=kinds)     

# @app.route("/kind/create", methods=["GET"])
# def get_kind_create():
#     return render_template("kind_create.html")

# @app.route("/kind/create", methods=["POST"])
# def post_kind_create():
#     data = dict(request.form)
#     database.create_pet(data)
#     return redirect(url_for("get_kind_list"))

# @app.route("/kind/delete/<id>", methods=["GET"])
# def get_kind_delete(id):
#     database.delete_pet(id)
#     return redirect(url_for("get_kind_list"))

# @app.route("/kind/update/<id>", methods=["GET"])
# def get_kind_update(id):
#     data = database.get_pet(id)
#     return render_template("kind_update.html",data=data)

# @app.route("/kind/update/<id>", methods=["POST"])
# def post_kind_update(id):
#     data = dict(request.form)
#     database.update_pet(id, data)
#     return redirect(url_for("get_kind_list"))
