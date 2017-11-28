from flask import Flask, render_template, request, redirect
app = Flask(__name__)

# Fake Data (TEMP)
# category = {'name': 'Dev Tools', 'id': '1'}
# categories = [
#   {'name': 'Dev Tools', 'id': '1'},
#   {'name': 'IDEs', 'id': '2'},
#   {'name': 'Documents', 'id': '3'},
# ]
# item = {
#     'name': 'Transmit',
#     'description': 'this is an app',
#     'image_url': 'transmit.png',
#     'website': 'https://panic.com/transmit/',
#     'id': '1'
#   }
# items = [
#   {
#     'name': 'Transmit',
#     'description': 'this is an app',
#     'image_url': 'transmit.png',
#     'website': 'https://panic.com/transmit/',
#     'id': '1'
#   },
#   {
#     'name': 'PyCharm',
#     'description': 'this is also an app',
#     'image_url': 'pycharm.png',
#     'website': 'https://www.jetbrains.com/pycharm/',
#     'id': '2'
#   },
#   {
#     'name': 'webstorm',
#     'description': 'yet another app. yay',
#     'image_url': 'webstorm.png',
#     'website': 'https://www.jetbrains.com/webstorm/',
#     'id': '3'
#   }
# ]


@app.route('/')
@app.route('/categories')
def showCategories():
  return render_template(
    'categories.html', categories=categories
  )

@app.route('/category/<int:category_id>')
@app.route('/category/<int:category_id>/items')
def showItemsList(category_id):
  return render_template(
    'itemlist.html', category=category, items=items
  )

@app.route('/category/new', methods=['GET', 'POST'])
def newCategory():
  if request.method == 'POST':
    newCategory = Category(name=request.form['name'])
    session.add(newCategory)
    session.commit()
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

@app.route('/category/<int:category_id>/item/<int:item_id>')
def itemDetails(category_id, item_id):
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