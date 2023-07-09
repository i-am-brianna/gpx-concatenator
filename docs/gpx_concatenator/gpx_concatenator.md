# GPXConcatenator

[Gpx-concatenator Index](../README.md#gpx-concatenator-index) /
[Gpx Concatenator](./index.md#gpx-concatenator) /
GPXConcatenator

> Auto-generated documentation for [gpx_concatenator.gpx_concatenator](../../gpx_concatenator/gpx_concatenator.py) module.

- [GPXConcatenator](#gpxconcatenator)
  - [GPXConcatenator](#gpxconcatenator-1)
    - [GPXConcatenator().concatenate_files](#gpxconcatenator()concatenate_files)

## GPXConcatenator

[Show source in gpx_concatenator.py:7](../../gpx_concatenator/gpx_concatenator.py#L7)

A class that concatenates multiple GPX files into a single GPX file.

#### Signature

```python
class GPXConcatenator:
    def __init__(
        self,
        input_files: List[str],
        output_file: str,
        enable_metadata: bool,
        enable_coloring: bool = False,
    ):
        ...
```

### GPXConcatenator().concatenate_files

[Show source in gpx_concatenator.py:27](../../gpx_concatenator/gpx_concatenator.py#L27)

Concatenates the input GPX files into a single GPX file.

#### Returns

None

#### Signature

```python
def concatenate_files(self):
    ...
```