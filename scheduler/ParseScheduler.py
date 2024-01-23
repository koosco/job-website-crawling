import time
import schedule


class ParseScheduler(schedule.Scheduler):
    def add_job(self, interval_minutes, job_function):
        job = schedule.every(interval_minutes).seconds.do(job_function)
        self.jobs.append(job)

    def run(self):
        while True:
            schedule.run_pending()
            time.sleep(1)
