import random
from datetime import datetime, timedelta
from db import log_production, init_db

PRODUCTS = ['iron_plate', 'copper_wire', 'electronic_circuit']
MACHINES = ['furnace_1', 'furnace_2', 'assembler_1', 'assembler_2']
START_DATE = datetime.now() - timedelta(days=7)
INTERVAL_MINUTES = 30
MAX_OUTPUT = 100

def generate_data():
    cur_time = START_DATE
    while cur_time <= datetime.now():
        if cur_time.hour >= 8 and cur_time.hour <= (10 + 12):
            utilization_rate = random.uniform(0.7, 0.95)
        else:
            utilization_rate = random.uniform(0.1, 0.4)

        product_name = random.choice(PRODUCTS)
        quantity = int(MAX_OUTPUT * utilization_rate)
        # !! should be limited by type
        assembler_id = random.choice(MACHINES)
        defect_count = random.randint(0, 5)
        lead_time = random.uniform(0.5, 5)
        log_production(product_name=product_name, quantity=quantity, assembler_id=assembler_id,
            utilization_rate=utilization_rate, defect_count=defect_count,lead_time=lead_time)

        cur_time += timedelta(minutes=INTERVAL_MINUTES)

if __name__ == "__main__":
    init_db()
    generate_data()