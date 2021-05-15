# CacheSimulationPlatform

To see examples of how to use library see src/example.py

## How to run
This simulation platform is designed as a library to be run from the terminal. 
There are 2 ways to run it:
1. Using a *quick run*. The `SimulationPlatform.run_simulations()` method is a quick way to run the platfrom using 
   some of the default zipfian request modal adn normally distributed file cost and parameter. See the example below from example.py
   
```python
def test():
    # Example of a quick run
    s = SimulationPlatform().run_simulations(
        ['RR', 'FIFO', 'LRU', 'LFU', 'LFU_IDEAL', 'MAD','MIN','MINAD'],
        n_iter=1,
        n_requests=999,
        cache_size=10,
        library_size=1000,
        performance_metric_names=['hit_ratio','latency_loss','simple_loss'],
        request_frq=1000,
        zipf_eta=1.5,
        seed = None)
```
2. The second way allows for a greater degree of control over the simulation. You must 
   explicitly outline each of the modals and build a simulation instance. This example can also be found in example.py
```python
def test_online_algorithms():
    performance_metric_names = ['hit_ratio','latency_loss','simple_loss']
    for algorithm in caching_algorithms_online:
        print('\t')
        # define instance parameters
        cache_size = 10
        library_size = 1000
        n_requests = 10000

        # set cache with its initial state
        virtual_cache = VirtualCache(np.random.choice(np.arange(0,library_size), size=cache_size, replace=False))

        # Create instances fro the request modals, library modals, caching algorithms adn perfromance metrc being simulated

        request_modal = request_modals.Zipfian(num_requests=n_requests, library_size=library_size, eta=1.7)

        library_modal = library_modals.StaticNormalCost(library_size, 100, 10)

        # Example of using get instead of a direct declaration (Note no request modal for online)
        caching_algorithm = caching_algorithms.get(algorithm, cache_size, library_modal) if caching_algorithms.is_online(algorithm) else caching_algorithms.get(algorithm, cache_size, library_modal, request_modal)

        # Create the instance recorder for the performance metrics to use
        recorder = Recorder()
        recorder.start(request_modal, virtual_cache.state(), library_modal)

        # Create and run the instance
        sim = SimulationInstance(caching_algorithm, recorder, request_modal, library_modal, virtual_cache)


        ## Simulate
        record = sim.simulate()
        for p,pm in zip(performance_metric_names,record.get_performances(performance_metric_names)):
            print(f'{algorithm}\t {p} : {pm.result}')

        # Post processing for the final result from the performance metric
    print('Done')
```

## Defining the Models

Outlined below are the abstract method that needs to be implemented in order to create a custom modal for the simulation platform. A significant amount of effort was put into designing the modal classes in such a way that they were easy to understand and implement for mathematically inclined non-programmer and the working of combing them into a single simulation was done behind the scenes.

All models implement the following `params()` function which allows parsing and batch simulation parsing.

```python
@property
def params() -> list[int]:
```
Returns a list of any additional initialisation parameters, the modal to be defined my take.


### Library Modal

```python
def cost(file: int) -> float:
```

The cost of bringing a file to the cache. Note that this function may update the library state allowing the simulation of variable latency caching.

```python
def size(file: int) -> float:
```

The size of a file in the library. Note that this function may also update the library state.

### Request Modal

```python
def _generate() -> Generator[float, int]:
```

A generator function that yields a tuple for each request in the sequence in the form $(time, file)$

### Performance Metric

```python
def record(time: float, replacement_address: int) -> None:
```

This function is called after every request and updates the performance metric state based on the time of the request and the replacement address given by the algorithm being simulates

Note that if  `replacment_address` is:

- `None` $\to$ cache hit
- `>= 0` $\to$ cache miss
- `-1` $\to$ the requested file was not cache, this is to allow for measuring performance in the *optional* policies setting

```python
def compute() -> None:
```

Called after the simulation is complete to perform any post-processing.

### Caching Algorithm

```python
def __call__(time: float, requested_file: int, cache_state: VirtualCache) -> int:
```

called by the cache simulation to simulate a request and returns the address of the file within the cache it decides to evict.

## Classes

### Library Modal
In the library model, we specify some of the priori assumptions on the caching problem we will be modelling.
Such as the size of the library along with the cost and size associated with each file.


### Request Sequence

Let us define a request for the file f at time t is represented by tuple `(f,t)` with type `Tuple[int,float]`.
We can consider this class to be a list of these pairs.