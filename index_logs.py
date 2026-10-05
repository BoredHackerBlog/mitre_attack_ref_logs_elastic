import glob
from evtxtoelk import EvtxToElk, ensure_index, iter_documents, make_client

es = make_client("http://localhost:9200")
ensure_index(es, "wineventlogs")

for file in glob.glob('evtx*/*.evtx'):
  print(file)
  result = EvtxToElk(es, index="wineventlogs", metadata={"evtx_file": file}).load(file)
  print(result.indexed, result.failed, result.skipped)
