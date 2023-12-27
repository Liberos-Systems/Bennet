from icecream import ic as original_ic
import datetime

def ic(*args, **kwargs):
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    log_message = f"<<{current_time}>> " + " ".join(map(str, args))
    try:
        original_ic(log_message, **kwargs)
    except Exception as e:
        original_ic(f"An error occurred: {e}")
