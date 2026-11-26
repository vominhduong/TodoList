from datetime import datetime
from time import timezone

from flask import Blueprint, redirect, render_template, request, url_for

from app import db
from app.models import Task

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    tasks = Task.query.order_by(Task.created_at.desc()).all()
    return render_template("index.html", tasks=tasks)


@bp.route("/tasks", methods=["POST"])
def create_task():
    title = request.form.get("title")
    if title.strip():
        task = Task(title=title, status='pending')
        db.session.add(task)
        db.session.commit()
    return redirect(url_for("main.index"))
    

@bp.route("/tasks/<int:task_id>/toggle", methods=["POST"])
def toggle_task(task_id):
    task = db.get_or_404(Task, task_id)
    if task.status == 'pending':
        task.status = 'completed'
    else:
        task.status = 'pending'
    db.session.commit()
    return redirect(url_for("main.index"))

@bp.route("/tasks/<int:task_id>/edit", methods=["POST"])
def edit_task(task_id):
    task = db.get_or_404(Task, task_id)
    new_title = request.form.get("title")
    if new_title.strip():
        task.title = new_title
        db.session.commit()
    return redirect(url_for("main.index"))

@bp.route("/tasks/<int:task_id>/delete", methods=["POST"])
def delete_task(task_id):
    task = db.get_or_404(Task, task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("main.index"))
# TODO: POST /tasks/<int:task_id>/toggle  -> đổi completed
# TODO: POST /tasks/<int:task_id>/edit    -> sửa title
# TODO: POST /tasks/<int:task_id>/delete  -> xoá task
# Gợi ý: task = db.get_or_404(Task, task_id)
