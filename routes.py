from flask import render_template, redirect, request, url_for
from datetime import datetime
from app import app, db
from models import Expense

@app.route('/')
def index():
    expenses = Expense.query.all()
    return render_template('index.html', expenses=expenses)

# Add a new expense
@app.route('/add', methods=['POST'])
def add_expense():
    name = request.form['expense_name']
    amount = float(request.form['amount'])
    date = datetime.strptime(request.form['date'], '%Y-%m-%d')

    new_expense = Expense(name=name, amount=amount, date=date)
    db.session.add(new_expense)
    db.session.commit()

    return redirect(url_for('index'))

# Delete an expense
@app.route('/delete/<int:id>')
def delete_expense(id):
    expense = Expense.query.get_or_404(id)
    db.session.delete(expense)
    db.session.commit()
    
    return redirect(url_for('index'))

# Update an expense
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_expense(id):
    expense = Expense.query.get_or_404(id)

    if request.method == 'POST':
        expense.name = request.form['expense_name']
        expense.amount = float(request.form['amount'])
        expense.date = datetime.strptime(request.form['date'], '%Y-%m-%d')
        
        db.session.commit()
        return redirect(url_for('index'))
    
    return render_template('update.html', expense=expense)