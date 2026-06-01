# React + Flask Portfolio Project

## Structure

- frontend/ -> React frontend
- backend/ -> Flask backend API

---

## Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

---

## Backend Setup

```bash
cd backend

python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate

pip install -r requirements.txt

python app.py
```

---

## Environment Variables

Create `.env` inside backend folder:

```env
PORT=5000
MONGO_URI=your_mongodb_connection_string
GROQ_API_KEY=your_groq_api_key
```
