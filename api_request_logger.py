# API Request Logger
import json
import time
from datetime import datetime
from urllib.request import urlopen

class APILogger:
    """
    Log API requests and responses
    """
    
    def __init__(self, log_file="api_requests.log"):
        self.log_file = log_file
        self.requests = []
    
    def log_request(self, method: str, url: str, status_code: int, response_time: float, response_data=None):
        """
        Log an API request with details
        """
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'method': method,
            'url': url,
            'status_code': status_code,
            'response_time_ms': response_time * 1000,
            'response_data': response_data
        }
        
        self.requests.append(log_entry)
        self._save_to_file(log_entry)
    
    def _save_to_file(self, log_entry: dict):
        """
        Save log entry to file
        """
        try:
            with open(self.log_file, 'a') as f:
                f.write(json.dumps(log_entry) + '\n')
        except Exception as e:
            print(f"Error writing to log file: {e}")
    
    def get_statistics(self):
        """
        Get statistics from logged requests
        """
        if not self.requests:
            return {}
        
        avg_response_time = sum(r['response_time_ms'] for r in self.requests) / len(self.requests)
        status_codes = {}
        
        for req in self.requests:
            code = req['status_code']
            status_codes[code] = status_codes.get(code, 0) + 1
        
        return {
            'total_requests': len(self.requests),
            'average_response_time_ms': avg_response_time,
            'status_code_distribution': status_codes
        }
    
    def print_report(self):
        """
        Print logged request report
        """
        stats = self.get_statistics()
        print("\n=== API REQUEST REPORT ===")
        print(f"Total Requests: {stats.get('total_requests', 0)}")
        print(f"Average Response Time: {stats.get('average_response_time_ms', 0):.2f}ms")
        print(f"Status Codes: {stats.get('status_code_distribution', {})}")

if __name__ == "__main__":
    print("API Request Logger v1.0")
    logger = APILogger()
    
    # Example: Log a test request
    logger.log_request("GET", "https://api.example.com/data", 200, 0.234, {"status": "success"})
    logger.print_report()
