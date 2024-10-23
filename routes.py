from flask import render_template, redirect, request
from datetime import datetime
from app import app, db
from models import Expense

@app.route('/') # Main page
def index():
    expenses = Expense.query.all()
    return render_template('index.html', expenses=expenses)


@app.route('/add', methods=['POST']) # add route
def add_expense():
    name = request.form['expense_name']
    amount = float(request.form['amount'])
    date = datetime.strptime(request.form['date'], '%Y-%m-%d')

    new_expense = Expense(name=name, amount=amount, date=date)
    db.session.add(new_expense)
    db.session.commit()

    return redirect('/')


@app.route('/delete/<id>') # delete route
def delete_expense(id):
    expense = Expense.query.get_or_404(id)
    db.session.delete(expense)
    db.session.commit()
    
    return redirect('/')

@app.route('/update/<id>', methods=['GET', 'POST']) # update route
def update_expense(id):
    expense = Expense.query.get_or_404(id)

    if request.method == 'POST':
        expense.name = request.form['expense_name']
        expense.amount = float(request.form['amount'])
        expense.date = datetime.strptime(request.form['date'], '%Y-%m-%d')
        
        db.session.commit()
        return redirect('/')
    
    return render_template('update.html', expense=expense)