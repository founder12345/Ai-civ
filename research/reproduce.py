"""Clean-room deterministic reproduction check for Nexus Research Release 1.0."""
import json, sys, hashlib
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[0] / 'src'))
from civ_lab.seed import build_default_simulation

def snap(s):
    x=s.stats()
    return {k:x.get(k) for k in ['tick','gdp','unemployment_rate','inflation','avg_happiness','avg_wealth','gini_estimate','housing_price_index','stock_market_index','poverty_rate','productivity_index']}

def digest(obj): return hashlib.sha256(json.dumps(obj,sort_keys=True).encode()).hexdigest()
checks=[]
for seed in [20260826,20260827,20260828,20260829,20260830]:
    a=build_default_simulation(30,6,seed); b=build_default_simulation(30,6,seed)
    a.step(360); b.step(360)
    checks.append({'seed':seed,'same':digest(snap(a))==digest(snap(b)),'digest':digest(snap(a))})
assert all(x['same'] for x in checks)
Path(__file__).with_name('reproduction_check.json').write_text(json.dumps({'status':'PASS','checks':checks},indent=2))
print('REPRODUCTION PASS',len(checks),'seeds')
