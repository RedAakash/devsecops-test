class LogAnalyzer:
    def __init__(self, log_file_path):
        self.log_file_path = log_file_path
        self.unique_get_ips = set()

    def extract_get_request_ips(self):
        with open(self.log_file_path, 'r') as log_file:
            for log_line in log_file:
                if '"GET' in log_line:
                    ip_address = log_line.split()[0]
                    self.unique_get_ips.add(ip_address)

    def save_sorted_ips_to_file(self, output_file_name):
        sorted_ip_list = sorted(self.unique_get_ips)
        with open(output_file_name, 'w') as output_file:
            for ip in sorted_ip_list:
                output_file.write(ip + '\n')

    def count_unique_ips(self):
        return len(self.unique_get_ips)

    def analyze(self, output_file_name='unique_ips.txt'):
        self.extract_get_request_ips()
        self.save_sorted_ips_to_file(output_file_name)
        total_ips = self.count_unique_ips()
        print(f"Total unique IPs that made GET requests: {total_ips}")

if __name__ == "__main__":
    log_file = "access.log"
    result_file = "unique_ips.txt"

    analyzer = LogAnalyzer(log_file)
    analyzer.analyze(output_file_name=result_file)
