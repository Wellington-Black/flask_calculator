from app import app
from modules.calculator import *

@app.route('/add/<num1>/<num2>')
def addition(num1, num2):
    answer = add(int(num1), int(num2))
    return "The answer is "+ f"{answer}"

@app.route('/sub/<num1>/<num2>')
def substraction(num1, num2):
    answer = sub(int(num1), int(num2))
    return "The answer is "+ f"{answer}"

@app.route('/mult/<num1>/<num2>')
def multiplication(num1, num2):
    answer = mult(int(num1), int(num2))
    return "The answer is "+ f"{answer}"

@app.route('/div/<num1>/<num2>')
def division(num1, num2):
    answer = div(int(num1), int(num2))
    return "The answer is "+ f"{answer}"
    
   
