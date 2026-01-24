from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
import os
from ..safety.opt_out import OptOutManager

app = FastAPI()
opt_out_manager = OptOutManager()

VERIFY_TOKEN = os.getenv("WHATSAPP_VERIFY_TOKEN", "default_token")

@app.get("/webhook")
async def verify_webhook(request: Request):
    params = request.query_params
    mode = params.get("hub.mode")
    token = params.get("hub.verify_token")
    challenge = params.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        return int(challenge)
    raise HTTPException(status_code=403, detail="Verification failed")

@app.post("/webhook")
async def handle_webhook(request: Request):
    data = await request.json()
    
    # Process incoming messages
    if "entry" in data:
        for entry in data["entry"]:
            for change in entry.get("changes", []):
                value = change.get("value", {})
                messages = value.get("messages", [])
                for message in messages:
                    sender_id = message.get("from")
                    if message.get("type") == "text":
                        text = message.get("text", {}).get("body", "")
                        # Check for opt-out request
                        if opt_out_manager.check_message_for_opt_out(sender_id, text):
                            print(f"User {sender_id} opted out.")
                    
                    # Log message status updates if needed
                    statuses = value.get("statuses", [])
                    for status in statuses:
                        print(f"Message {status.get('id')} status: {status.get('status')}")

    return {"status": "success"}
