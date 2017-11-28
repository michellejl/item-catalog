from flask import Flask, render_template, request, redirect
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item

app = Flask(__name__)

engine = create_engine('sqlite:///categoryitems.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# View all Categories
@app.route('/')
@app.route('/categories')
def showCategories():
  categories = session.query(Category).all()
  return render_template(
    'categories.html', categories=categories
  )

# View all Items in a Specified Category
@app.route('/category/<int:category_id>')
@app.route('/category/<int:category_id>/items')
def showItemsList(category_id):
  category = session.query(Category).filter_by(id=category_id).one()
  items = session.query(Item).filter_by(category_id=category_id).all()
  return render_template(
    'itemlist.html', category=category, items=items
  )

@app.route('/category/new', methods=['GET', 'POST'])
def newCategory():
  if request.method == 'POST':
    return redirect(url_for('showCategories'))
  else:
    return render_template('newcategory.html')

@app.route('/category/<int:category_id>/edit', methods=['GET', 'POST'])
def editCategory(category_id):
  if request.method == 'POST':
    return redirect(url_for('showCategories'))
  else:
    return render_template('editcategory.html', category=category)

@app.route('/category/<int:category_id>/delete')
def deleteCategory(category_id):
  if request.method == 'POST':
    return redirect(url_for('showCategories'))
  else:
    return render_template('deletecategory.html', category=category)

# View details of a selected item
@app.route('/category/<int:category_id>/item/<int:item_id>')
def itemDetails(category_id, item_id):
  category = session.query(Category).filter_by(id=category_id).one()
  item = session.query(Item).filter_by(id=item_id).one()
  return render_template(
    'item.html', category=category, item=item
  )

@app.route('/category/<int:category_id>/item/new')
def newItem(category_id):
  if request.method == 'POST':
    newItem = Item(name=request.form['name'])
    session.add(newCategory)
    session.commit()
    return redirect(url_for('showItemsList', category_id = category.id))
  else:
    return render_template('newitem.html', category=category)

@app.route('/category/<int:category_id>/item/<int:item_id>/edit')
def editItem(category_id, item_id):
  if request.method == 'POST':
    return redirect(url_for('showItemsList'))
  else:
    return render_template('editItem.html', category=category, item=item)

@app.route('/category/<int:category_id>/item/<int:item_id>/delete')
def deleteItem(category_id, item_id):
  if request.method == 'POST':
    return redirect(url_for('showItemsList'))
  else:
    return render_template('deleteitem.html', category=category, item=item)




if __name__ == '__main__':
  app.debug = True
  app.run(host = '0.0.0.0', port = 5000)