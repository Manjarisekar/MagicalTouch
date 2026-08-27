from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/book', methods=['POST'])
def book_appointment():
    data = request.get_json()
    name = data.get('name')
    phone = data.get('phone')
    service = data.get('service')
    date = data.get('date')
    
    return jsonify({
        "status": "success",
        "message": f"Thank you {name}! Your booking for {service} on {date} has been received. We will contact you at {phone}."
    })

if __name__ == '__main__':
    app.run(debug=True)