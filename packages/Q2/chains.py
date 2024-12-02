# Reference for using the Chain class in Django Q
from django_q.tasks import async_chain, Chain, result_group
import math


# Example 1: Using async_chain directly
def async_chain_example():
    # Chain of tasks: each task has a function, arguments, and optional kwargs
    chain = [
        ("math.copysign", (1, -1)),  # First task: math.copysign
        ("math.floor", (1,)),  # Second task: math.floor
    ]

    # Run the chain asynchronously
    group_id = async_chain(chain)

    # Fetch the result for the chain after it's processed (limit results to 2)
    results = result_group(group_id, count=2)
    print(f"Results from async_chain: {results}")


# Example 2: Using the Chain class with append and caching enabled
def chain_class_example():
    # Create a Chain instance with caching enabled
    chain = Chain(cached=True)

    # Append tasks to the chain
    chain.append("math.copysign", 1, -1)  # Task 1: math.copysign
    chain.append("math.floor", 1)  # Task 2: math.floor
    chain.append("math.sqrt", 16)  # Task 3: math.sqrt

    # Run the chain
    group_id = chain.run()
    print(f"Chain started with group ID: {group_id}")

    # Fetch the results of the chain
    results = chain.result()  # Returns the results after tasks finish
    print(f"Results from Chain instance: {results}")

    # Use additional methods to retrieve task status and results
    print(f"Current task index: {chain.current()}")
    print(f"Total number of tasks in the chain: {chain.length()}")


# Example 3: Running the tasks synchronously and handling failures
def sync_chain_example():
    # Create a Chain instance with sync=True
    chain = Chain(sync=True)

    # Append tasks to the chain (this will run synchronously)
    chain.append("math.copysign", 1, -1)
    chain.append("math.floor", 1)
    chain.append("math.sqrt", -1)  # This will raise an error

    # Run the chain and get the results (synchronously)
    results = chain.result(wait=5000)  # Wait up to 5 seconds for results
    print(f"Results from sync chain (with failure handling): {results}")

    # Fetch detailed information about failed tasks
    failed_tasks = chain.fetch(failures=True)
    print(f"Failed tasks: {failed_tasks}")


# Example 4: Using the group feature for organization
def group_chain_example():
    # Create a chain with a group name for easy tracking
    chain = Chain(group="math_operations")

    # Append tasks to the chain
    chain.append("math.copysign", 1, -1)
    chain.append("math.floor", 1)

    # Run the chain and get the group ID
    group_id = chain.run()
    print(f"Group ID for the chain: {group_id}")

    # Fetch the results of the group
    results = result_group(group_id, count=2)
    print(f"Group results: {results}")


if __name__ == "__main__":
    # Run examples
    async_chain_example()
    chain_class_example()
    sync_chain_example()
    group_chain_example()
