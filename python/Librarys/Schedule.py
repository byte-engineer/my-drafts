import schedule
import time

def job():
    print("Running the app at the scheduled time!")


# Schedule the job at 2:30 PM every day
schedule.every().day.at("14:30").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
