from apscheduler.schedulers.background import BackgroundScheduler, BlockingScheduler
import time
from datetime import datetime

scheduler = BackgroundScheduler()


# scheduler = BlockingScheduler()


def scheduled_task():
    print(f"I'm scheduled to run now: {datetime.now()}")


def start_scheduler():
    print("Scheduler is about to start...")
    scheduler.add_job(scheduled_task, "interval", seconds=5)
    scheduler.start()
    print("Scheduler is started...")


def stop_scheduler():
    scheduler.shutdown()
