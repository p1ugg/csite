from flask import Flask, request, jsonify
from sklearn.linear_model import LinearRegression
import numpy as np

app = Flask(__name__)

# Пример обученной модели
model = LinearRegression()
X_train = np.array([[0], [1], [2], [3]])
y_train = np.array([0, 1, 2, 3])
model.fit(X_train, y_train)

@app.route('/process', methods=['POST'])
def process():
    data = request.json
    X_test = np.array(data['features']).reshape(-1, 1)
    prediction = model.predict(X_test)
    result = {'model2_result': prediction.tolist()}
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
