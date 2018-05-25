from prometheus_client import start_http_server
from prometheus_client.core import GaugeMetricFamily, REGISTRY
import speedtest, time


class STCollector(object):
    def collect(self):
        print "{} Collecting metric".format(time.time())
        s.download()
        s.upload()
        results_dict = s.results.dict()
        metrics = {'pingms': GaugeMetricFamily("speedtest_ping", "ping to speedtest.net", labels=["target"]), 'upload': GaugeMetricFamily("speedtest_upload", "upload speed to speedtest.net", labels=["target"]), 'download': GaugeMetricFamily("speedtest_download", "download speed to speedtest.net", labels=["target"])}
        print "{} metric {}".format(time.time(), results_dict)
        host = results_dict['server']['host']
        metrics['pingms'].add_metric([host], results_dict['ping'])
        metrics['upload'].add_metric([host], results_dict['upload'])
        metrics['download'].add_metric([host], results_dict['download'])
        for metric_name, metric in metrics.items():
            yield metric

if __name__ == '__main__':
    s = speedtest.Speedtest()
    s.get_best_server()
    start_http_server(8090)
    REGISTRY.register(STCollector())
    while True: time.sleep(1)
