from fastapi import APIRouter, UploadFile, File, Form, HTTPException, Depends
from app.services.assistant_service import create_assistant, create_vector_store, upload_file, fetch_vector_stores, start_run,update_assistant,send_message,retrieve_messages,create_thread,list_assistants

# Define the router
assistant_router = APIRouter()

@assistant_router.post("/create")
async def create_assistant_route():
    return create_assistant()

@assistant_router.get("/assistant/vector_store/list", tags=["Vector Store"])
async def get_vector_stores():
    return fetch_vector_stores()

@assistant_router.post("/assistant/vector_store/upload")
async def upload_file_route(vector_store_id: str = Form(...), file: UploadFile = File(...)):
    try:
        file_path = "C:\\Projects\\Planck\\Phase 1\\vector_store\\Lumdarian Crystal web app.txt"
        with open(file_path, "wb") as f:
            f.write(file.file.read())

        return upload_file(vector_store_id, file_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@assistant_router.post("/assistant/update")
async def update_assistant_route(assistant_id: str, vector_store_id: str):
    return update_assistant(assistant_id, vector_store_id)

@assistant_router.post("/assistant/thread/create")
def create_thread_route():
    return create_thread()

@assistant_router.post("/assistant/message")
def send_message_route(thread_id: str = Form(...), content: str = Form(...)):
    return send_message(thread_id, content)

@assistant_router.get("/assistant/messages")
def retrieve_messages_route(thread_id: str, run_id: str):
    return retrieve_messages(thread_id, run_id)

@assistant_router.post("/assistant/thread/run")
def start_run_route(thread_id: str):
    return start_run(thread_id)

@assistant_router.get("/assistant/list")
def list_assistants_route():
    return list_assistants()

# Main router
router = APIRouter()
router.include_router(assistant_router, prefix="/assistant", tags=["Assistant"])
