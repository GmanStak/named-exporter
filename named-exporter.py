import json, socket, prometheus_client
from prometheus_client import Gauge
from prometheus_client.core import CollectorRegistry
from flask import Response, Flask
from gevent import pywsgi
from arguments import get_args


app = Flask(__name__)

REGISTRY = CollectorRegistry(auto_describe=False)

domain_status = Gauge("dmoain_status", "域名解析", ['domain','domain_ip', 'hostname', 'dns_ip'],registry=REGISTRY)

args = get_args()
config_path = args.config
def get_json(config_path):
    with open(config_path) as json_file:
        config = json.load(json_file)
        return config

def get_domain(doman):
    try:
        domain_ip = socket.gethostbyname(doman)
        return domain_ip
    except socket.error:
        return False

config_list = get_json(config_path)
domain_status.clear()
for domain in config_list:
    result = get_domain(domain['domain'])
    if result:
        domain_status.labels(domain=domain['domain'],domain_ip=result,hostname=domain['hostname'],dns_ip=domain['dns_ip']).set(1)
    else:
        domain_status.labels(domain=domain['domain'],domain_ip='None',hostname=domain['hostname'],dns_ip=domain['dns_ip']).set(0)

@app.route('/')
def index():
    return "<h1>Customized Exporter</h1><br> <a href='metrics'>Metrics</a>"

@app.route('/metrics')
def dns_status():
    return Response(prometheus_client.generate_latest(REGISTRY),mimetype="text/plain")

if __name__=='__main__':
    # app.run(host='0.0.0.0', port=9088, threaded=True)
    host = args.ipaddress
    port = args.port
    server = pywsgi.WSGIServer((host, port), app)
    server.serve_forever()
