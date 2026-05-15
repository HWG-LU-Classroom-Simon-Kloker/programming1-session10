from relief_worker import ReliefWorker

worker = ReliefWorker('Clara', 'Barton', 40000)
print(f"Initial salary: ${worker.annual_salary}")
worker.give_raise()
print(f"After raise: ${worker.annual_salary}")
