from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('trained_model.pkl')

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get user input from the form
    mean_radius = float(request.form['mean_radius'])
    mean_texture = float(request.form['mean_texture'])
    mean_perimeter = float(request.form['mean_perimeter'])
    mean_area = float(request.form['mean_area'])
    mean_smoothness = float(request.form['mean_smoothness'])
    mean_compactness = float(request.form['mean_compactness'])
    mean_concavity = float(request.form['mean_concavity'])
    mean_concave_points = float(request.form['mean_concave_points'])
    mean_symmetry = float(request.form['mean_symmetry'])
    mean_fractal_dimension = float(request.form['mean_fractal_dimension'])
    radius_error = float(request.form['radius_error'])
    texture_error = float(request.form['texture_error'])
    perimeter_error = float(request.form['perimeter_error'])
    area_error = float(request.form['area_error'])
    smoothness_error = float(request.form['smoothness_error'])
    compactness_error = float(request.form['compactness_error'])
    concavity_error = float(request.form['concavity_error'])
    concave_points_error = float(request.form['concave_points_error'])
    symmetry_error = float(request.form['symmetry_error'])
    fractal_dimension_error = float(request.form['fractal_dimension_error'])
    worst_radius = float(request.form['worst_radius'])
    worst_texture = float(request.form['worst_texture'])
    worst_perimeter = float(request.form['worst_perimeter'])
    worst_area = float(request.form['worst_area'])
    worst_smoothness = float(request.form['worst_smoothness'])
    worst_compactness = float(request.form['worst_compactness'])
    worst_concavity = float(request.form['worst_concavity'])
    worst_concave_points = float(request.form['worst_concave_points'])
    worst_symmetry = float(request.form['worst_symmetry'])
    worst_fractal_dimension = float(request.form['worst_fractal_dimension'])

    # Prepare the input data as a list
    feature_vector = [[mean_radius, mean_texture, mean_perimeter, mean_area, mean_smoothness,
                   mean_compactness, mean_concavity, mean_concave_points, mean_symmetry,
                   mean_fractal_dimension, radius_error, texture_error, perimeter_error,
                   area_error, smoothness_error, compactness_error, concavity_error,
                   concave_points_error, symmetry_error, fractal_dimension_error,
                   worst_radius, worst_texture, worst_perimeter, worst_area, worst_smoothness,
                   worst_compactness, worst_concavity, worst_concave_points, worst_symmetry,
                   worst_fractal_dimension]]

    # Perform prediction using the loaded model
    prediction = model.predict(feature_vector)

    # Prepare the prediction result message
    if prediction[0] == 0:
        result = "Benign"
    else:
        result = "Malignant"

    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
