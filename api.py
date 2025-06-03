from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/cnc-data")
def get_cnc_data():
    return {
        "avanco": round(random.uniform(50, 300), 2),             # mm/min
        "rpm": random.randint(500, 10000),                            #RPM
        "profundidade": round(random.uniform(0.5, 5.0), 2),      # mm
        "mttr": round(random.uniform(1, 5), 2),                   # horas
        "mttf": round(random.uniform(10, 50), 2),                 # horas
        "ff": round(random.uniform(0.1, 1.0), 2),                 # fator de falha
        "corrente_motor": round(random.uniform(5, 20), 2),       # A
        "tensao_motor": round(random.uniform(200, 240), 2),      # V
        "vibracao_fuso": round(random.uniform(0.1, 3.0), 2),     # mm/s
        "vibracao_ferramenta": round(random.uniform(0.1, 3.0), 2) # mm/s
    }
