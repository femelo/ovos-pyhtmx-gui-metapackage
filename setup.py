from setuptools import setup, find_packages

setup(
    name="ovos-pyhtmx-gui-metapackage",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "ovos-gui @ git+https://github.com/femelo/ovos-gui.git@add-pyhtmx-system-pages",
        "ovos-audio @ git+https://github.com/femelo/ovos-audio.git@add-audio-duration",
        "ovos-dinkum-listener @ git+https://github.com/femelo/ovos-dinkum-listener.git@add-audio-duration-to-master",
        "ovos-skill-homescreen @ git+https://github.com/femelo/ovos-skill-homescreen.git@add-pyhtmx-gui-resources",
        "ovos-ocp-audio-plugin @ git+https://github.com/femelo/ovos-ocp-audio-plugin.git@add-pyhtmx-resources",
        "ovos-skill-date-time @ git+https://github.com/femelo/ovos-skill-date-time.git@add-pyhtmx-time-page",
        "ovos-skill-weather @ git+https://github.com/femelo/ovos-skill-weather.git@add-units-to-weather-params",
        "pyhtmx-gui-client @ git+https://github.com/femelo/pyhtmx-gui-client.git@extract-homescreen-resources",
    ],
    author="Flavio De Melo",
    author_email="flavio.eler@gmail.com",
    description="Metapackage for OVOS PyHTMX GUI components",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    python_requires=">=3.8",
)