import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

print(os.getenv("DB_URL"))

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("app.api:app", host="0.0.0.0", port=port, reload=True)

