# Caching

- Information copied from slower to faster storage
- Faster storage is checked first to determine if information is there
    - if it is, uses cache
    - if not, copy data to cache and use there

## Consistency and Coherency

Same data may appear in different levels. Changing the copy in register make it inconsistent with other copies.

- Single task : no problem
- Multi task : need to obtain the most recent value
- Distributed system: really difficult
