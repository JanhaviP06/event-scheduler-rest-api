# 🗓️ Event Scheduler System

A simple REST API built with **Python Flask** for scheduling events with CRUD and search functionality.  
This system allows users to **create, view, update, delete, and search events** efficiently.

---

## 🚀 **Features**

✅ Create an event with title, description, start time, end time, and optional recurrence  
✅ View all scheduled events sorted by start time  
✅ Update event details  
✅ Delete events  
✅ Search events by title or description (case-insensitive)  
✅ Data persistence using **SQLite database**

---

## 🛠️ **Tech Stack**

- **Backend:** Python 3.x, Flask, SQLAlchemy  
- **Database:** SQLite  
- **API Testing:** Postman

---

## 📁 **Project Structure**

```bash
event_scheduler/
├── app/
│ ├── init.py
│ ├── models.py
│ ├── routes.py
├── run.py
├── requirements.txt
└── event_scheduler_collection.json

```
---

## ⚙️ **Setup Instructions**

### **1. Clone the repository**

```bash
git clone https://github.com/JanhaviP06/event-scheduler-rest-api.git
cd event_scheduler
```
2. Create virtual environment and activate
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Mac/Linux
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Run the application
```bash
python run.py
✅ The server will start at http://127.0.0.1:5000/
```

## 📝 API Endpoints

### **Create Event**

- **POST** `/events`

**Body (JSON):**

```json
{
  "title": "Meeting",
  "description": "Discuss project deliverables",
  "start_time": "2025-07-01 10:00",
  "end_time": "2025-07-01 11:00",
  "recurrence": "daily"  // optional: daily, weekly, monthly
}
```
---
### **Get All Events**

- **GET** `/events`

---

### **Update Event**

- **PUT** `/events/<event_id>`

**Body (JSON):**

```json
{
  "title": "Updated Meeting",
  "description": "Updated description"
}
```
---
### **Delete Event**

- **DELETE** `/events/<event_id>`

---

### **Search Events**

- **GET** `/events/search?query=<search_term>`

**Example:** /events/search?query=meeting
---

--- 

## 🔗 Postman Collection

✅ Import the provided `event_scheduler_collection.json` file in Postman to test all endpoints.

---

## 🎯 Future Enhancements

- Reminders for events due within the next hour (checked every minute)
- Recurring events generation automation
- Email notifications for event reminders
- Dockerization for deployment
- CI/CD integration with GitHub Actions

---

## 👩‍💻 Author

**Janhavi Phulavare**  
_Data Analyst & Python Developer_

---

## ⭐ Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
