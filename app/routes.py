from flask import Blueprint, request, jsonify
from datetime import datetime
from .models import Event
from sqlalchemy import func
from . import db

events_bp = Blueprint('events', __name__)

@events_bp.route('/')
def home():
    return jsonify({"message": "Event Scheduler API is running"}), 200

# Create Event
@events_bp.route('/events', methods=['POST'])
def create_event():
    data = request.json

    required_fields = ['title', 'description', 'start_time', 'end_time']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f"{field} is required"}), 400

    # Validate datetime formats
    try:
        datetime.strptime(data['start_time'], "%Y-%m-%d %H:%M")
        datetime.strptime(data['end_time'], "%Y-%m-%d %H:%M")
    except ValueError:
        return jsonify({'error': 'Invalid datetime format. Use YYYY-MM-DD HH:MM'}), 400

    # Validate recurrence if provided
    recurrence = data.get('recurrence')
    valid_recurrences = [None, 'daily', 'weekly', 'monthly']
    if recurrence not in valid_recurrences:
        return jsonify({'error': 'Invalid recurrence. Choose daily, weekly, monthly, or omit'}), 400

    event = Event(
        title=data['title'],
        description=data['description'],
        start_time=data['start_time'],
        end_time=data['end_time'],
        recurrence=recurrence
    )

    db.session.add(event)
    db.session.commit()

    return jsonify({
        "message": "Event created successfully",
        "event": event.to_dict()
    }), 201

# Get All Events
@events_bp.route('/events', methods=['GET'])
def get_events():
    events = Event.query.order_by(Event.start_time).all()
    event_list = [e.to_dict() for e in events]

    return jsonify({
        "total_events": len(event_list),
        "events": event_list
    }), 200

# Update Event
@events_bp.route('/events/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    data = request.json
    event = Event.query.get(event_id)

    if not event:
        return jsonify({'error': 'Event not found'}), 404

    for field in ['title', 'description', 'start_time', 'end_time', 'recurrence']:
        if field in data:
            if field in ['start_time', 'end_time']:
                try:
                    datetime.strptime(data[field], "%Y-%m-%d %H:%M")
                except ValueError:
                    return jsonify({'error': f'Invalid {field} format. Use YYYY-MM-DD HH:MM'}), 400
            if field == 'recurrence':
                valid_recurrences = [None, 'daily', 'weekly', 'monthly']
                if data[field] not in valid_recurrences:
                    return jsonify({'error': 'Invalid recurrence. Choose daily, weekly, monthly, or omit'}), 400
            setattr(event, field, data[field])

    db.session.commit()

    return jsonify({
        "message": "Event updated successfully",
        "event": event.to_dict()
    }), 200


# Delete Event
@events_bp.route('/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    event = Event.query.get(event_id)

    if not event:
        return jsonify({'error': 'Event not found'}), 404

    db.session.delete(event)
    db.session.commit()

    return jsonify({'message': f'Event with id {event_id} deleted successfully'}), 200


#search event
@events_bp.route('/events/search', methods=['GET'])
def search_events():
    query = request.args.get('query')

    if not query:
        return jsonify({'error': 'Query parameter is required'}), 400

    query_lower = query.lower()

    results = Event.query.filter(
        (func.lower(Event.title).contains(query_lower)) |
        (func.lower(Event.description).contains(query_lower))
    ).order_by(Event.start_time).all()

    return jsonify({
        "total_results": len(results),
        "events": [e.to_dict() for e in results]
    }), 200
