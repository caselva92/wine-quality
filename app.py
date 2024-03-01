from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Define route for serving the index.html file
@app.route('/')
def index():
    return render_template('index.html')

# Define route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Get feature values from the request
    fixed_acidity = float(request.form['fixed_acidity'])
    volatile_acidity = float(request.form['volatile_acidity'])
    citric_acid = float(request.form['citric_acid'])
    residual_sugar = float(request.form['residual_sugar'])
    chlorides = float(request.form['chlorides'])
    free_sulfur_dioxide = float(request.form['free_sulfur_dioxide'])
    total_sulfur_dioxide = float(request.form['total_sulfur_dioxide'])
    density = float(request.form['density'])
    pH = float(request.form['pH'])
    sulphates= float(request.form['sulphates'])
    alcohol = float(request.form['alcohol'])

    # Make prediction (replace this with your own prediction logic)
    predicted_quality = fixed_acidity + volatile_acidity + citric_acid + residual_sugar + chlorides + free_sulfur_dioxide + total_sulfur_dioxide + density + pH + sulphates + alcohol

    # Return prediction as JSON response
    return jsonify({'predicted_quality': predicted_quality})

if __name__ == '__main__':
    app.run(debug=True)