import os
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL'] + 'tasks'
print(SQLALCHEMY_DATABASE_URI)

# from os.path import abspath, dirname, join

# from logging import debug
# from flask import Flask, render_template, url_for, request, redirect, flash, Markup
# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime
# import os


# __cwd = dirname(abspath(__file__))

# SECRET_KEY = os.environ.get("TODO-App_Secret-Key")
# SQLALCHEMY_DATABASE_URI = "sqlite:///" + join(__cwd, "tasks.db")
# # SQLALCHEMY_DATABASE_URI = 'postgresql://' + os.environ['Postgres_Username'] + ':' + os.environ['Postgres_Password'] + '@localhost/tasks'
# SQLALCHEMY_ECHO = True
# WTF_CSRF_SECRET_KEY = os.environ.get("TODO-App_WTF-CSRF")  #'this-should-be-more-random'

# app = Flask(__name__, template_folder="templates")
# app.config.from_object(__name__)

# db = SQLAlchemy(app)


# class Site(db.Model):
#     __tablename__ = "tasks"

#     id = db.Column(db.Integer, primary_key=True)
#     task = db.Column(db.String(150), nullable=False)
#     completed = db.Column(db.Integer, default=0)
#     date_created = db.Column(db.DateTime, default=datetime.now)

#     def __repr__(self):
#         return "<Task %r>" % self.id

#     def __str__(self):
#         return self.base_url


# @app.route("/", methods=["GET"])  #
# def index():
#     # if request.method == "POST":
#     #     task_content = request.form["task"]
#     #     new_task = ToDo(task=task_content)

#     #     try:
#     #         db.session.add(new_task)
#     #         db.session.commit()
#     #         return redirect("/")

#     #     except:
#     #         return "There was a problem adding your task!"

#     # else:
#     #     tasks = ToDo.query.order_by(ToDo.date_created).all()
#     return render_template("index.html")  # , tasks=tasks)


# # @app.route("/delete/<int:id>")
# # def delete(id):
# #     task_to_delete = ToDo.query.get_or_404(id)

# #     try:
# #         db.session.delete(task_to_delete)
# #         db.session.commit()
# #         return redirect("/")
# #     except:
# #         return "There was a problem deleting the task!"


# if __name__ == "__main__":
#     app.run(debug=True)
