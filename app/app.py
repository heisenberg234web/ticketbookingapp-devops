from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Mock database for tickets
tickets = []
ticket_id_counter = 1

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/tickets', methods=['GET'])
def get_tickets():
    return jsonify(tickets)

@app.route('/api/tickets', methods=['POST'])
def book_ticket():
    global ticket_id_counter
    data = request.json
    
    ticket = {
        'id': ticket_id_counter,
        'event': data.get('event'),
        'name': data.get('name'),
        'email': data.get('email'),
        'quantity': data.get('quantity'),
        'price': data.get('price', 50)
    }
    
    tickets.append(ticket)
    ticket_id_counter += 1
    
    return jsonify(ticket), 201

@app.route('/api/tickets/<int:ticket_id>', methods=['DELETE'])
def cancel_ticket(ticket_id):
    global tickets
    tickets = [t for t in tickets if t['id'] != ticket_id]
    return jsonify({'message': 'Ticket cancelled'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)