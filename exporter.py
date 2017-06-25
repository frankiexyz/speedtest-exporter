from prometheus_client import start_http_server
from prometheus_client.core import GaugeMetricFamily, REGISTRY
import pyspeedtest, time


class STCollector(object):
    def collect(self):
        print "{} Collecting metric".format(time.time())
        metrics = {'pingms': GaugeMetricFamily("speedtest_ping", "ping to speedtest.net", labels=["target"]), 'upload': GaugeMetricFamily("speedtest_upload", "upload speed to speedtest.net", labels=["target"]), 'download': GaugeMetricFamily("speedtest_download", "download speed to speedtest.net", labels=["target"])}
        metrics['pingms'].add_metric([host], st.ping())
        metrics['upload'].add_metric([host], st.upload())
        metrics['download'].add_metric([host], st.download())
        for metric_name, metric in metrics.items():
            yield metric

if __name__ == '__main__':
    st = pyspeedtest.SpeedTest()
    host =  st.host
    start_http_server(8090)
    REGISTRY.register(STCollector())
    while True: time.sleep(1)
