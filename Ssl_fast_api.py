from fastapi import FastAPI
import uvicorn
import ssl

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, world!"}

if __name__ == "__main__":
    ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    ssl_context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1  # Ensure only TLSv1.2 is used
    uvicorn.run(app, host="0.0.0.0", port=5000, ssl_keyfile="key.pem", ssl_certfile="cert.pem", ssl_version=ssl.PROTOCOL_TLSv1_2)

