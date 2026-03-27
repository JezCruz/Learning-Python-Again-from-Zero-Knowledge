# Data Validation Tool
import re
from typing import List, Dict, Any

class DataValidator:
    """
    Utility class for validating various data types
    """
    
    @staticmethod
    def validate_email(email: str) -> bool:
        """Validate email format"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    @staticmethod
    def validate_phone(phone: str) -> bool:
        """Validate phone number format"""
        pattern = r'^\+?1?\d{9,15}$'
        return re.match(pattern, phone.replace('-', '').replace(' ', '')) is not None
    
    @staticmethod
    def validate_url(url: str) -> bool:
        """Validate URL format"""
        pattern = r'^https?://[^\s]+$'
        return re.match(pattern, url) is not None
    
    @staticmethod
    def validate_ipv4(ip: str) -> bool:
        """Validate IPv4 address"""
        parts = ip.split('.')
        if len(parts) != 4:
            return False
        try:
            return all(0 <= int(part) <= 255 for part in parts)
        except ValueError:
            return False
    
    @staticmethod
    def validate_credit_card(card_num: str) -> bool:
        """Validate credit card number using Luhn algorithm"""
        card_num = card_num.replace(' ', '').replace('-', '')
        if not card_num.isdigit() or len(card_num) < 13:
            return False
        
        digits = [int(d) for d in card_num]
        checksum = 0
        for i, digit in enumerate(reversed(digits)):
            if i % 2 == 1:
                digit *= 2
                if digit > 9:
                    digit -= 9
            checksum += digit
        return checksum % 10 == 0

def validate_data_set(data: List[Dict[str, Any]], schema: Dict[str, str]) -> List[Dict]:
    """
    Validate a set of data against a schema
    Returns list of validation results
    """
    validator = DataValidator()
    results = []
    
    for idx, record in enumerate(data):
        record_result = {'index': idx, 'valid': True, 'errors': []}
        
        for field, field_type in schema.items():
            if field not in record:
                record_result['errors'].append(f"Missing field: {field}")
                record_result['valid'] = False
                continue
            
            value = record[field]
            
            if field_type == 'email':
                if not validator.validate_email(value):
                    record_result['errors'].append(f"Invalid email: {value}")
                    record_result['valid'] = False
            elif field_type == 'phone':
                if not validator.validate_phone(value):
                    record_result['errors'].append(f"Invalid phone: {value}")
                    record_result['valid'] = False
            elif field_type == 'url':
                if not validator.validate_url(value):
                    record_result['errors'].append(f"Invalid URL: {value}")
                    record_result['valid'] = False
        
        results.append(record_result)
    
    return results

if __name__ == "__main__":
    print("Data Validation Tool")
    validator = DataValidator()
    
    # Test examples
    print(f"Email test@example.com: {validator.validate_email('test@example.com')}")
    print(f"URL https://github.com: {validator.validate_url('https://github.com')}")
    print(f"IPv4 192.168.1.1: {validator.validate_ipv4('192.168.1.1')}")
