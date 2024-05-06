# https://oxylabs.io/blog/concurrency-vs-parallelism
# Threading: CPU switches between different threads really fast, giving a falsehood of concurrency. Keypoint: only one thread is running at any given time. When one thread is running, others are blocked. You might think, how is this any useful than just running procedurally? Well, think of it as a priority queue. Threads can be scheduled. CPU scheduler can give each thread a certain amount of time to run, pause them, pass data to other threads, then give them different priorities to run at a later time. It's a must for not instant running processes that interact with each other. It's used in servers extensively: thousands of clients can request something at the same time, then getting what they requested at a later time (If done procedurally, only one client can be served at a time). Philosophy: do different things together. It doesn't reduce the total time (moot point for server, because one client doesn't care other clients' total requests).

# Parallelism: threads are running parallel, usually in different CPU core, true concurrency. Keypoint: mlutiple threads are running at any given time. It's useful for heavy computations, super long running processes. Same thing with a fleet of single core machines, split data into sections for each machine to compute, pool them together at the end. Different machines/cores are hard to interact with each other. Philosophy: do one thing in less time.



# Concurrency: 交替执行， 做一会儿A，等待的时候做一会B，再等待的时候再做A，做一件事时是可中断的

# parallelism： 并行执行
import time
from multiprocessing import Pool, cpu_count
from concurrent.futures import ThreadPoolExecutor
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_links():
    countries_list = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population'

    all_links = []

    response = requests.get(countries_list)

    soup = BeautifulSoup(response.text, "lxml")

    countries_el = soup.select('td .flagicon+ a')

    for link_el in countries_el:
        link = link_el.get('href')
        link = urljoin(countries_list, link)
        all_links.append(link)

    return all_links

def fetch(link):
    response = requests.get(link)

    with open(link.split('/')[-1]+'.html', 'wb') as f:
        f.write(response.content)


if __name__ == '__main__':
    links = get_links()
    print(f'Total page: {len(links)}')

    start_time = time.time()

    # This for loop will be optimized (sync)
    # for link in links:
    #     fetch(link)
    
    # use concurrency/threading method (async), only need 1 core
    # with ThreadPoolExecutor(max_workers=10) as executor:
    #     executor.map(fetch, links)
    
    # use parallelism/mutli-processing method (async), need multi cores
    with Pool(cpu_count()) as p: # processes in pool are decided by the number of cores of this computer (my mac is 10 cores)
        p.map(fetch, links)

    duration = time.time() - start_time

    print(f'Downloaded {len(links)} links in {duration} seconds')

