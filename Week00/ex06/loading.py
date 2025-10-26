import time
import sys

def ft_progress(lst):
    """
    A function that displays the progress of a for loop.
    
    Args:
        lst: An iterable object.
    
    Yields:
        Each element from lst one by one.
    """
    total = len(lst)
    start_time = time.time()
    
    for i, item in enumerate(lst):
        elapsed_time = time.time() - start_time
        
        # Calculate percentage
        percent = (i + 1) / total * 100
        
        # Calculate ETA (Estimated Time of Arrival)
        if i == 0:
            eta = 0
        else:
            eta = (elapsed_time / (i + 1)) * (total - i - 1)
        
        # Create progress bar
        bar_length = 20
        filled_length = int(bar_length * (i + 1) / total)
        bar = '=' * filled_length + '>' + ' ' * (bar_length - filled_length - 1)
        
        # Print progress
        sys.stdout.write(f"\rETA: {eta:.2f}s [{percent:3.0f}%][{bar}] {i+1}/{total} | elapsed time {elapsed_time:.2f}s")
        sys.stdout.flush()
        
        yield item

# Example usage:
if __name__ == "__main__":
    # Test 1
    listy = range(9)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        time.sleep(0.01)
    print()
    print(ret)
    
    # Test 2
    # listy = range(3333)
    # ret = 0
    # for elem in ft_progress(listy):
    #     ret += elem
    #     time.sleep(0.005)
    # print()
    # print(ret)
