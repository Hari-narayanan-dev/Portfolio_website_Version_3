from dotenv import load_dotenv
import os
load_dotenv()

MONGO_URI = os.getenv("MONGO_URL")
CONTACT_DATABASE_NAME = "Portfolio_data"
CONTACT_COLLECTION_NAME = "portfolio_contact_form"

