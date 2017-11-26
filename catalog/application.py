from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/categories')
def showCategories():
  return "Category list"

@app.route('/category/<int:category_id>')
@app.route('/category/<int:category_id>/items')
def showItemsList():
  return "Items list"

@app.route('/category/new')
def newCategory():
  return "New Category"

@app.route('/category/<int:category_id>/edit')
def editCategory():
  return "Edit Category"

@app.route('/category/<int:category_id>/delete')
def deleteCategory():
  return "Delete Category"

@app.route('/category/<int:category_id>/item/<int:item_id>')
def itemDetails():
  return "Item Details"

@app.route('/category/<int:category_id>/item/new')
def newItem():
  return "New Item"

@app.route('/category/<int:category_id>/item/<int:item_id>/edit')
def editItem():
  return "Edit Item"

@app.route('/category/<int:category_id>/item/<int:item_id>/delete')
def deleteItem():
  return "Delete Item"




if __name__ == '__main__':
  app.debug = True
  app.run(host = '0.0.0.0', port = 5000)