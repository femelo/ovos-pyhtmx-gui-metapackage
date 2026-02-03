# OVOS PyHTMX GUI Metapackage

This project defines a metapackage that consolidates several OVOS components for setting up a development
environment for the PyHTMX GUI client.

## Installation

To install this metapackage and all its dependencies, you can use pip:

```bash
pip install .
```

This will install the following packages from their respective GitHub branches:

- `ovos-gui@add-pyhtmx-system-pages`
- `ovos-audio@add-audio-duration`
- `ovos-dinkum-listener@add-audio-duration-to-master`
- `ovos-skill-homescreen@add-pyhtmx-gui-resources`
- `ovos-plugin-common-play@add-pyhtmx-resources`
- `ovos-skill-date-time@add-pyhtmx-time-page`
- `ovos-skill-weather@add-units-to-weather-params`
- `ovos-pyhtmx-gui-client@extract-homescreen-resources`
