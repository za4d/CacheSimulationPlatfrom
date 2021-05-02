<!-- Quartz Smokey -->

# **Backdoor** run platform

## Customizable Parameters

- Caching algorithm
- Request modal
- Communication modal
- Performance metric

## Hyperparameters

> Note that each is a list

- (Caching Algorithms, list of Caching algorithms arguments as KWDs) [^1]
- (Request modal, list of Request modal arguments as KWDs)
- (Communication modal, list of Communication modal arguments as KWDs)
- (Performance metric, list of Performance metric arguments as KWDs)
- *number of iterations to average over*
- *number of requests to simulate*
- *size of cache*
- *size of library*
- seed
- *Z is a communiation modal parameter*
- *eta is a request modal parameter*
- *hit weight and miss weight are performance metric parameters*



[^1]: list of tuple containing names and parameters as keyword dictionaries e.g.

```python
[
    ('hit-ratio', 
     [{ hit-count: 0, miss-count: 0}, { hit-count: 1000, miss-count: 10}, ...]
    ),
    ('gain', 
     [{ hit-weight: 1, miss-weigth: 1}, { hit-weight: 5, miss-weigth: 2}, ...]
    ), ...
]
```

## Instance Parameters

- Caching Algorithm 
- *Caching algorithms arguments kwd*
- Request modal
- *Request modal arguments kwd*
- Communication modal
- *Communication modal arguments kwd*
- Performance metric
- *Performance metric arguments kwd*
- number of iterations to average over
- number of requests to simulate
- size of cache
- size of library
- seed

## Converting hyperparameters into list of instance parameters

1. convert customizable variables
   1. expand each tuple of name and list of kwd to name and kwd

      `(name, [kwd1,kwd2,...]) -> [(name,kwd1),(name,kwd2),(name,kwd3),...]`

   2. do this for each name in list than concatenate the lists

2. Take the cross product of all lists to return a list of instance parameters to simulate



# Simple run for platform
## Hyperparameters

> Note that each is NOT a list except for the algorithms

- List of (Caching Algorithms, Caching algorithms arguments as KWDs) [^1]
- single Request modal, Request modal arguments as KWDs
- single Communication modal, Communication modal arguments as KWDs
- single Performance metric, Performance metric arguments as KWDs
- number of iterations to average over
- number of requests to simulate
- size of cache
- size of library
- seed



# Customisable Variables

- stored as packages
- each package `__init__.py` containing `__all__` definition and a `get` function that converts each

