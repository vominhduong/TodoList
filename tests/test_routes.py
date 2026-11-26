import pytest

from app import create_app, db
from app.models import Task
from config import TestConfig


@pytest.fixture
def app():
    app = create_app(TestConfig)
    yield app
    with app.app_context():
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


def add(app, title, status="pending"):
    with app.app_context():
        task = Task(title=title, status=status)
        db.session.add(task)
        db.session.commit()
        return task.id


def get(app, task_id):
    with app.app_context():
        return db.session.get(Task, task_id)


def test_index_empty(client):
    res = client.get("/")
    assert res.status_code == 200
    assert "Chưa có công việc nào" in res.get_data(as_text=True)


def test_create_task(app, client):
    res = client.post("/tasks", data={"title": "  Mua sữa  "}, follow_redirects=True)
    assert res.status_code == 200
    with app.app_context():
        tasks = Task.query.all()
        assert len(tasks) == 1
        assert tasks[0].title == "Mua sữa"
        assert tasks[0].status == "pending"
        assert tasks[0].created_at is not None


@pytest.mark.parametrize("data", [{}, {"title": ""}, {"title": "   "}, {"title": "x" * 101}])
def test_create_task_invalid(app, client, data):
    res = client.post("/tasks", data=data, follow_redirects=True)
    assert res.status_code == 200
    with app.app_context():
        assert Task.query.count() == 0


def test_toggle_task(app, client):
    task_id = add(app, "A")
    client.post(f"/tasks/{task_id}/toggle")
    assert get(app, task_id).status == "completed"
    client.post(f"/tasks/{task_id}/toggle")
    assert get(app, task_id).status == "pending"


def test_edit_task(app, client):
    task_id = add(app, "Cũ")
    client.post(f"/tasks/{task_id}/edit", data={"title": "Mới"})
    assert get(app, task_id).title == "Mới"
    client.post(f"/tasks/{task_id}/edit", data={"title": " "})
    assert get(app, task_id).title == "Mới"


def test_delete_task(app, client):
    task_id = add(app, "A")
    client.post(f"/tasks/{task_id}/delete")
    assert get(app, task_id) is None


def test_missing_task_returns_404(client):
    assert client.post("/tasks/999/toggle").status_code == 404
    assert client.post("/tasks/999/edit", data={"title": "x"}).status_code == 404
    assert client.post("/tasks/999/delete").status_code == 404


def test_filter_and_search(app, client):
    add(app, "Học Flask")
    add(app, "Đi chợ", status="completed")
    html = client.get("/?status=completed").get_data(as_text=True)
    assert "Đi chợ" in html and "Học Flask" not in html
    html = client.get("/?q=flask").get_data(as_text=True)
    assert "Học Flask" in html and "Đi chợ" not in html


def test_clear_completed(app, client):
    keep = add(app, "A")
    add(app, "B", status="completed")
    client.post("/tasks/clear-completed")
    with app.app_context():
        assert [t.id for t in Task.query.all()] == [keep]


def test_redirect_keeps_filter(app, client):
    task_id = add(app, "A")
    res = client.post(f"/tasks/{task_id}/toggle?status=pending&q=A")
    assert res.status_code == 302
    assert "status=pending" in res.location and "q=A" in res.location
