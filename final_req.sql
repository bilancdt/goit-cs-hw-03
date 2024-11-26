--Отримати всі завдання певного користувача:
SELECT * FROM tasks WHERE user_id = 1;

--Вибрати завдання за статусом:
SELECT * FROM tasks WHERE status_id = (SELECT id FROM status WHERE name = 'new');

--Оновити статус завдання:
UPDATE tasks SET status_id = (SELECT id FROM status WHERE name = 'in progress') WHERE id = 1;

--Користувачі без завдань:
SELECT * FROM users WHERE id NOT IN (SELECT user_id FROM tasks);

--Додати нове завдання для користувача:
INSERT INTO tasks (title, description, status_id, user_id)
VALUES ('New Task', 'Description of the task', 1, 2);

--Незавершені завдання:
SELECT * FROM tasks WHERE status_id != (SELECT id FROM status WHERE name = 'completed');

--Видалити завдання за ID:
DELETE FROM tasks WHERE id = 1;

--Користувачі з певною електронною поштою:
SELECT * FROM users WHERE email LIKE '%@example.com';

--Кількість завдань для кожного статусу:
SELECT status.name, COUNT(*) AS task_count
FROM tasks
JOIN status ON tasks.status_id = status.id
GROUP BY status.name;