import time
import multiprocessing

def do_something():
    print('sleeping for 1 second')
    time.sleep(1)
    print('Done sleeping')
def multiprocess():
    start = time.perf_counter()
    processes=[]
    for _ in range(10):
        p= multiprocessing.Process(target=do_something)
        p.start()
        processes.append(p)

    for p in processes:
        p.join()    #wait for the process to finish

    finish=time.perf_counter()
    print(f'finish in {round(finish-start,2)} seconds')
if __name__ == '__main__':
    multiprocess()
