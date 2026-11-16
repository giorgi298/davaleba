import time
import threading
import multiprocessing


# DAV 1
# def make_tea(name, seconds):
#     print(f"{name}: იწყება")
#     time.sleep(seconds)
#     print(f"{name}: მზადაა")
#
# teas = [("მწვანე ჩაი", 1.0), ("შავი ჩაი", 1.5), ("ბალახის ჩაი", 2.0)]
#
# start_seq = time.time()
# for name, secs in teas:
#     make_tea(name, secs)
# end_seq = time.time()
# seq_time = end_seq - start_seq
# print(f"თანმიმდევრულად: {seq_time:.1f} წმ")
#
# start_threads = time.time()
# threads = []
# for name, secs in teas:
#     t = threading.Thread(target=make_tea, args=(name, secs))
#     threads.append(t)
#     t.start()
#
# for t in threads:
#     t.join()
# end_threads = time.time()
# thread_time = end_threads - start_threads
# print(f"thread-ებით: {thread_time:.1f} წმ")
#
# speedup = seq_time / thread_time if thread_time > 0 else 0
# print(f"აჩქარება: {speedup:.1f}x")

# რატომ უდრის thread ების დრო დაახლოებით ყველაზე ხანგრძლივი ჩაის დროს?
# იმიტომ რომ ყველა thread იწყება ერთდროულად და მუშაობს პარალელურად
# და საერთო დასრულება დამოკიდებულია ყველაზე ნელ ამოცანაზე.


# DAV 2

# def cpu_task(n):
#     while n > 0:
#         n -= 1
#
# def io_task(seconds):
#     time.sleep(seconds)
#
# def measure(runner, task, jobs):
#     start = time.time()
#     runner(task, jobs)
#     return time.time() - start
#
# def run_sequential(task, jobs):
#     for job in jobs:
#         task(job)
#
# def run_threads(task, jobs):
#     threads = [threading.Thread(target=task, args=(job,)) for job in jobs]
#     for t in threads:
#         t.start()
#     for t in threads:
#         t.join()
#
# def run_processes(task, jobs):
#     processes = [multiprocessing.Process(target=task, args=(job,)) for job in jobs]
#     for p in processes:
#         p.start()
#     for p in processes:
#         p.join()
#
# if __name__ == '__main__':
#     cpu_jobs = [10_000_000] * 4
#     io_jobs = [1.0] * 4
#
#     print("\nCPU-bound:")
#     seq_cpu = measure(run_sequential, cpu_task, cpu_jobs)
#     th_cpu = measure(run_threads, cpu_task, cpu_jobs)
#     pr_cpu = measure(run_processes, cpu_task, cpu_jobs)
#     print(f"თანმიმდევრულად: {seq_cpu:.2f} წმ (1.0x)")
#     print(f"thread-ებით: {th_cpu:.2f} წმ ({seq_cpu/th_cpu:.1f}x)")
#     print(f"პროცესებით: {pr_cpu:.2f} წმ ({seq_cpu/pr_cpu:.1f}x)")
#
#     print("\nI/O-bound:")
#     seq_io = measure(run_sequential, io_task, io_jobs)
#     th_io = measure(run_threads, io_task, io_jobs)
#     pr_io = measure(run_processes, io_task, io_jobs)
#     print(f"თანმიმდევრულად: {seq_io:.2f} წმ (1.0x)")
#     print(f"thread-ებით: {th_io:.2f} წმ ({seq_io/th_io:.1f}x)")
#     print(f"პროცესებით: {pr_io:.2f} წმ ({seq_io/pr_io:.1f}x)")

# რატომ არ აჩქარდა cpu-bound ამოცანა thread-ებით და რატომ აჩქარდა i/o-bound ამოცანა?
# cpu-bound ამოცანის დროს Pythonში global interpreter lock ზღუდავს ერთდროულად მრავალი თრედის მუშაობას პროცესორზე
# რის გამოც თრედები ცალცალკე ვერ იყენებენ მრავალ ბირთვს.
# i/o-bound ამოცანის დროს კი time.sleep() ათავისუფლებს gil-ს რაც საშუალებას აძლევს თრედებს პარალელურად დაელოდონ შეფერხებებს.