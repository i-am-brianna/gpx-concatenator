# GPXFile

[Gpx-concatenator Index](../README.md#gpx-concatenator-index) /
[Gpx Concatenator](./index.md#gpx-concatenator) /
GPXFile

> Auto-generated documentation for [gpx_concatenator.gpx_file](../../gpx_concatenator/gpx_file.py) module.

- [GPXFile](#gpxfile)
  - [GPXFile](#gpxfile-1)
    - [GPXFile().extract_metadata](#gpxfile()extract_metadata)
    - [GPXFile().extract_tracks](#gpxfile()extract_tracks)

## GPXFile

[Show source in gpx_file.py:4](../../gpx_concatenator/gpx_file.py#L4)

A class that represents a GPX file and provides methods for extracting metadata and tracks.

#### Signature

```python
class GPXFile:
    def __init__(self, file_path: str):
        ...
```

### GPXFile().extract_metadata

[Show source in gpx_file.py:19](../../gpx_concatenator/gpx_file.py#L19)

Extracts the metadata element from the GPX file.

#### Returns

- `ET.Element` - The metadata element if found, otherwise an empty metadata element.

#### Signature

```python
def extract_metadata(self) -> ET.Element:
    ...
```

### GPXFile().extract_tracks

[Show source in gpx_file.py:31](../../gpx_concatenator/gpx_file.py#L31)

Extracts the track elements from the GPX file.

#### Returns

- `List[ET.Element]` - A list of track elements.

#### Signature

```python
def extract_tracks(self) -> List[ET.Element]:
    ...
```