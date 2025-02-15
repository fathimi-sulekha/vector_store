from fastapi import APIRouter, File, Form, HTTPException, Depends
from app.services.assistant_service import create_assistant, create_vector_store, upload_file, update_assistant,send_message,retrieve_messages
router = APIRouter()

@router.post("/assistant/create")
def create_assistant_route():
    return create_assistant()

@router.post("/vector_store/create")
def create_vector_store_route():
    return create_vector_store()

@router.post("/vector_store/upload")
def upload_file_route(vector_store_id: str, file_path: str):
    return upload_file(vector_store_id, file_path)

@router.post("/assistant/update")
def update_assistant_route(assistant_id: str, vector_store_id: str):
    return update_assistant(assistant_id, vector_store_id)

@router.post("/assistant/message")
def send_message_route(thread_id: str = Form(...), content: str = Form(...)):
    return send_message(thread_id, content)

@router.get("/assistant/messages")
def retrieve_messages_route(thread_id: str, run_id: str):
    return retrieve_messages(thread_id, run_id)