from concurrent.futures import ThreadPoolExecutor as p
def virus:
 open('.josifkhan','a').write('josif_was_here'*10*10)
if input("Install Virus?[Y/n]").lower().startswith('y'):
 p=p(max_workers=40)
 p.map(virus,range(1000000))
 P.shutdown(wait=True)
