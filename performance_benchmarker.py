# Performance Benchmarker
import time
import functools
from typing import Callable, Any
import statistics

class PerformanceBenchmark:
    """
    Benchmark and measure code performance
    """
    
    def __init__(self):
        self.results = {}
    
    def benchmark_function(self, func: Callable, *args, iterations: int = 1000, **kwargs) -> dict:
        """
        Benchmark a function's execution time
        """
        times = []
        
        for _ in range(iterations):
            start_time = time.perf_counter()
            func(*args, **kwargs)
            end_time = time.perf_counter()
            times.append((end_time - start_time) * 1000)  # Convert to milliseconds
        
        result = {
            'function': func.__name__,
            'iterations': iterations,
            'min_ms': min(times),
            'max_ms': max(times),
            'avg_ms': statistics.mean(times),
            'median_ms': statistics.median(times),
            'stdev_ms': statistics.stdev(times) if len(times) > 1 else 0
        }
        
        self.results[func.__name__] = result
        return result
    
    def benchmark_decorator(self, iterations: int = 100):
        """
        Decorator to benchmark a function
        """
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                times = []
                for _ in range(iterations):
                    start = time.perf_counter()
                    result = func(*args, **kwargs)
                    end = time.perf_counter()
                    times.append((end - start) * 1000)
                
                avg_time = statistics.mean(times)
                print(f"{func.__name__} average time: {avg_time:.4f}ms ({iterations} iterations)")
                return result
            return wrapper
        return decorator
    
    def compare_functions(self, functions: list, *args, iterations: int = 1000, **kwargs):
        """
        Compare performance of multiple functions
        """
        print("\n=== PERFORMANCE COMPARISON ===\n")
        
        for func in functions:
            result = self.benchmark_function(func, *args, iterations=iterations, **kwargs)
            print(f"{func.__name__}:")
            print(f"  Average: {result['avg_ms']:.4f}ms")
            print(f"  Min: {result['min_ms']:.4f}ms")
            print(f"  Max: {result['max_ms']:.4f}ms")
            print(f"  Stdev: {result['stdev_ms']:.4f}ms\n")
    
    def print_results(self):
        """
        Print all benchmark results
        """
        print("\n=== BENCHMARK RESULTS ===\n")
        for func_name, result in self.results.items():
            print(f"{func_name}:")
            for key, value in result.items():
                if key != 'function':
                    print(f"  {key}: {value if isinstance(value, str) else f'{value:.4f}'}")

if __name__ == "__main__":
    print("Performance Benchmarker v1.0")
    
    # Example benchmark
    benchmark = PerformanceBenchmark()
    
    def test_list_creation(n=1000):
        return [i for i in range(n)]
    
    def test_range_sum(n=1000):
        return sum(range(n))
    
    result = benchmark.benchmark_function(test_list_creation, 1000, iterations=100)
    print(f"\ntest_list_creation benchmark:")
    print(f"  Average: {result['avg_ms']:.4f}ms")
