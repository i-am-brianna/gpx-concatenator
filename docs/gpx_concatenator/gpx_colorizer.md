# GPXColorizer

[Gpx-concatenator Index](../README.md#gpx-concatenator-index) /
[Gpx Concatenator](./index.md#gpx-concatenator) /
GPXColorizer

> Auto-generated documentation for [gpx_concatenator.gpx_colorizer](../../gpx_concatenator/gpx_colorizer.py) module.

- [GPXColorizer](#gpxcolorizer)
  - [GPXColorizer](#gpxcolorizer-1)
    - [GPXColorizer().add_coloring_metadata](#gpxcolorizer()add_coloring_metadata)
    - [GPXColorizer().colorize_tracks](#gpxcolorizer()colorize_tracks)

## GPXColorizer

[Show source in gpx_colorizer.py:5](../../gpx_concatenator/gpx_colorizer.py#L5)

A class that colorizes GPX tracks in XML format.

#### Signature

```python
class GPXColorizer:
    def __init__(self):
        ...
```

### GPXColorizer().add_coloring_metadata

[Show source in gpx_colorizer.py:81](../../gpx_concatenator/gpx_colorizer.py#L81)

Adds coloring metadata to the root element.

#### Arguments

- `root` *ET.Element* - The root element of the GPX XML.

#### Returns

None

#### Signature

```python
def add_coloring_metadata(self, root: ET.Element) -> None:
    ...
```

### GPXColorizer().colorize_tracks

[Show source in gpx_colorizer.py:17](../../gpx_concatenator/gpx_colorizer.py#L17)

Colorizes the tracks with distinct colors.

#### Arguments

- `tracks` *List[ET.Element]* - A list of track elements.

#### Returns

None

#### Signature

```python
def colorize_tracks(self, tracks: List[ET.Element]) -> None:
    ...
```