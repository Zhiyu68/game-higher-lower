from flask import Flask
import random

# 3. Generate a random number between 0 and 9
random_number = random.randint(0, 9)
print(random_number)

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"


@app.route("/<int:guess>")
def guess_number(guess):
    if guess > random_number:
        return "<h1 style='color: purple'>Too high, try again! Please!</h1>" \
               "<img src='https://media4.giphy.com/media/VWwS82FgMKRm8/giphy.gif?cid=ecf05e47oz2zse6vzb9lng22pkgy1ychae3pi5issqx5oge4&rid=giphy.gif&ct=g'/>"

    elif guess < random_number:
        return "<h1 style='color: red'>Too low, try again! Please!</h1>"\
               "<img src='https://media3.giphy.com/media/wdh1SvEn0E06I/giphy.gif?cid=ecf05e47qxjwnlqj3jejaweippopjul47bhmm9mh1f058xru&rid=giphy.gif&ct=g'/>"
    else:
        return "<h1 style='color: green'>Yeah! You found me!</h1>" \
               "<img src='https://media0.giphy.com/media/TdfyKrN7HGTIY/giphy.gif?cid=ecf05e47n555f8q3dhprepi2nbmc5hdyxeyh7wsv7fnchrkh&rid=giphy.gif&ct=g'/>"


if __name__ == "__main__":
    app.run(debug=True)