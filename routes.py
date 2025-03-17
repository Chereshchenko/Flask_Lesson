from flask import Flask

# Создаем объект приложения Flask
app = Flask(__name__)

# Определяем маршрут и привязываем его к функции
@app.route("/hello")
def hello():
    return "Hello, world!"

@app.route("/info")
def info():
    return "This is an informational page."

@app.route("/calc/<int:a>/<int:b>")
def calc(a, b):
    return f"The sum of {a} and {b} is {a + b}."

@app.errorhandler(404)
def not_found(error):
    return "Введите корректные целые числа.", 404

@app.route("/reverse/<word>")
def reverse(word):
    if len(word) < 2:
        return f"В слове 1 буква"
    return f"{word} - {''.join(reversed(word))}"

@app.route("/user/<name>/<int:age>")
def user(name, age):
    if age <= 0:
        return "Возрост не может быть меньше 0"
    return f"Hello, {name}. You are {age} years old."

# Запуск приложения
if __name__ == "__main__":
    app.run(debug=True)


