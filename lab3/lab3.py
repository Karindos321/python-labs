import time
import threading
from datetime import datetime, timedelta

scheduled_tasks = []

def schedule(time_spec):

    def decorator(func):
        if isinstance(time_spec, str):

            target_time = datetime.strptime(time_spec, '%H:%M:%S').time()
            now = datetime.now()
            first_run = datetime.combine(now.date(), target_time)
            
            if first_run < now:
                first_run += timedelta(days=1)
            interval = (first_run - now).total_seconds()
        else:
            interval = time_spec

        def wrapper(*args, **kwargs):
            func(*args, **kwargs)
            if isinstance(time_spec, (int, float)):
                
                scheduled_tasks.append((time.time() + interval, wrapper))
        scheduled_tasks.append((time.time() + interval, wrapper))
        return wrapper
    return decorator

def event_loop():
    while True:
        now = time.time()
        for task in scheduled_tasks[:]:
            run_time, func = task
            if now >= run_time:
                func()
                scheduled_tasks.remove(task)
        yield
        time.sleep(1)

@schedule('08:30:00')
def midnight_task():
    print("Вставай і йди в універ")

@schedule(2)
def repeat_task():
    print("Повторюю кожні 2 секунди")

def start_event_loop():
    loop = event_loop()
    while True:
        next(loop)

threading.Thread(target=start_event_loop, daemon=True).start()
while True:
    time.sleep(1)
