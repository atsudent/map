from apscheduler.schedulers.blocking import BlockingScheduler

def start_cron_job(func, hour, minute):
  print(f"Starting cron job - {hour}:{minute}")
  scheduler = BlockingScheduler()
  scheduler.add_job(func, 'cron', hour=hour, minute=minute)

  try:
    scheduler.start()
  except (KeyboardInterrupt):
    print('Shutting down...')
