from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Temporary storage for bookings
bookings = []

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/book', methods=['POST'])
def book():
    data = request.json  # Get JSON data from the frontend
    name = data.get("name")
    email = data.get("email")
    date = data.get("date")
    room_type = data.get("room_type")
    
    booking = {"id": len(bookings) + 1, "name": name, "email": email, "date": date, "room_type": room_type}
    bookings.append(booking)
    
    return jsonify({"message": "Booking successful", "booking": booking})

@app.route('/bookings', methods=['GET'])
def get_bookings():
    return jsonify(bookings)

@app.route('/book/<int:booking_id>', methods=['PUT'])
def update_booking(booking_id):
    data = request.json
    for booking in bookings:
        if booking["id"] == booking_id:
            booking.update(data)
            return jsonify({"message": "Booking updated", "booking": booking})
    return jsonify({"error": "Booking not found"}), 404

@app.route('/book/<int:booking_id>', methods=['DELETE'])
def delete_booking(booking_id):
    global bookings
    bookings = [b for b in bookings if b["id"] != booking_id]
    return jsonify({"message": "Booking deleted"})

if __name__ == '__main__':
    app.run()
