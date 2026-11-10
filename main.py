from fastapi import FastAPI

app = FastAPI(title="kyc-service", version="1.0.0")

@app.get("/actuator/health")
def health(): return {"status": "UP"}

@app.get("/kycs")
def route_0(): return {"status": "ok"}

@app.post("/kycs")
def route_1(): return {"status": "ok"}

@app.get("/kycs/{id}")
def route_2(): return {"status": "ok"}
