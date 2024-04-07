from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cdab0d1d0545bf48@m146564'

class ProductForm(FlaskForm):
    sku = StringField('SKU', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    sales_price = DecimalField('Sales Price', validators=[DataRequired()])
    purchase_price = DecimalField('Purchase Price', validators=[DataRequired()])
    submit = SubmitField('Submit')

class ClientForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    shipping_address = StringField('Shipping Address', validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired()])
    submit = SubmitField('Submit')

class LocationForm(FlaskForm):
    abbreviation = StringField('Abbreviation', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    product_form = ProductForm()
    client_form = ClientForm()
    location_form = LocationForm()
    if product_form.validate_on_submit() and client_form.validate_on_submit() and location_form.validate_on_submit():
        # Получаем данные из форм и передаем их в API Megaventory
        product_sku = product_form.sku.data
        product_description = product_form.description.data
        product_sales_price = product_form.sales_price.data
        product_purchase_price = product_form.purchase_price.data
        
        client_name = client_form.name.data
        client_email = client_form.email.data
        client_shipping_address = client_form.shipping_address.data
        client_phone = client_form.phone.data
        
        location_abbreviation = location_form.abbreviation.data
        location_name = location_form.name.data
        location_address = location_form.address.data
        
        # Далее взаимодействие с API Megaventory
        return 'Data submitted successfully.'
    return render_template('index.html', product_form=product_form, client_form=client_form, location_form=location_form)

if __name__ == '__main__':
    app.run(debug=True)


