from flask import Blueprint, flash, redirect, render_template, request, url_for

from app import db
from app.models import STATUS_COMPLETED, STATUS_PENDING, TITLE_MAX_LENGTH, Task

bp = Blueprint("main", __name__)

VALID_FILTERS = ("all", STATUS_PENDING, STATUS_COMPLETED)


def _clean_title(raw):
    """Chuẩn hoá và kiểm tra title. Trả về (title, error)."""
    title = (raw or "").strip()
    if not title:
        return None, "Tiêu đề không được để trống."
    if len(title) > TITLE_MAX_LENGTH:
        return None, f"Tiêu đề tối đa {TITLE_MAX_LENGTH} ký tự."
    return title, None


def _back_to_index():
    """Quay về trang chủ, giữ nguyên bộ lọc / từ khoá tìm kiếm hiện tại."""
    args = {}
    status = request.args.get("status")
    q = request.args.get("q")
    if status in VALID_FILTERS and status != "all":
        args["status"] = status
    if q:
        args["q"] = q
    return redirect(url_for("main.index", **args))


@bp.route("/")
def index():
    status = request.args.get("status", "all")
    if status not in VALID_FILTERS:
        status = "all"
    q = request.args.get("q", "").strip()

    query = Task.query
    if status != "all":
        query = query.filter(Task.status == status)
    if q:
        query = query.filter(Task.title.ilike(f"%{q}%"))
    tasks = query.order_by(Task.created_at.desc(), Task.id.desc()).all()

    counts = {
        "all": Task.query.count(),
        STATUS_PENDING: Task.query.filter_by(status=STATUS_PENDING).count(),
        STATUS_COMPLETED: Task.query.filter_by(status=STATUS_COMPLETED).count(),
    }
    return render_template(
        "index.html", tasks=tasks, status=status, q=q, counts=counts
    )


@bp.route("/tasks", methods=["POST"])
def create_task():
    title, error = _clean_title(request.form.get("title"))
    if error:
        flash(error, "danger")
    else:
        db.session.add(Task(title=title, status=STATUS_PENDING))
        db.session.commit()
        flash("Đã thêm công việc.", "success")
    return _back_to_index()


@bp.route("/tasks/<int:task_id>/toggle", methods=["POST"])
def toggle_task(task_id):
    task = db.get_or_404(Task, task_id)
    task.toggle()
    db.session.commit()
    return _back_to_index()


@bp.route("/tasks/<int:task_id>/edit", methods=["POST"])
def edit_task(task_id):
    task = db.get_or_404(Task, task_id)
    title, error = _clean_title(request.form.get("title"))
    if error:
        flash(error, "danger")
    else:
        task.title = title
        db.session.commit()
        flash("Đã cập nhật công việc.", "success")
    return _back_to_index()


@bp.route("/tasks/<int:task_id>/delete", methods=["POST"])
def delete_task(task_id):
    task = db.get_or_404(Task, task_id)
    db.session.delete(task)
    db.session.commit()
    flash("Đã xoá công việc.", "success")
    return _back_to_index()


@bp.route("/tasks/clear-completed", methods=["POST"])
def clear_completed():
    deleted = Task.query.filter_by(status=STATUS_COMPLETED).delete()
    db.session.commit()
    flash(f"Đã xoá {deleted} công việc đã hoàn thành.", "success")
    return _back_to_index()
