from app.dependencies.openai_services import get_openai_client

openai_client = get_openai_client()

def create_assistant():
    return openai_client.beta.assistants.create(
        instructions="Use the file provided as your knowledge base to best respond to customer queries",
        model="gpt-4o-mini",
        tools=[{"type": "file_search"}]
    )

def fetch_vector_stores():
    return openai_client.beta.vector_stores.list()

def create_vector_store():
    return openai_client.beta.vector_stores.create(name="Financial Report")

def upload_file(vector_store_id, file_path):
    with open(file_path, "rb") as file_stream:
        return openai_client.beta.vector_stores.file_batches.upload_and_poll(
            vector_store_id=vector_store_id, files=[file_stream]
        )

def update_assistant(assistant_id, vector_store_id):
    return openai_client.beta.assistants.update(
        assistant_id=assistant_id,
        tool_resources={"file_search": {"vector_store_ids": [vector_store_id]}}
    )

def create_thread():
    return openai_client.beta.threads.create()

def start_run(thread_id):
    return openai_client.beta.threads.runs.create(thread_id=thread_id, assistant_id="asst_jH8AJo5avoKnItcylD5yupbl")

def send_message(thread_id, content):
    return openai_client.beta.threads.messages.create(
        thread_id=thread_id, role="user", content=content
    )

def retrieve_messages(thread_id, run_id):
    return list(openai_client.beta.threads.messages.list(thread_id=thread_id, run_id=run_id))

def list_assistants():
    return openai_client.beta.assistants.list()
