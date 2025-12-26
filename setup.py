from setuptools import setup, find_packages

plugin_identifier = "prettygcode2026"
plugin_package = "octoprint_prettygcode"
plugin_name = "PrettyGCode 2026"
plugin_version = "1.2.4.1.quantenkosmos"
plugin_description = "A GCode visualizer - Quantenkosmos Patched"
plugin_author = "Kragrathea (original), Quantenkosmos (patched)"
plugin_url = "https://github.com/Kragrathea/OctoPrint-PrettyGCode" # Original repo
plugin_license = "AGPLv3"
plugin_additional_packages = []
plugin_requires = ["OctoPrint>=1.8.0"]

setup(
    name=plugin_name,
    version=plugin_version,
    description=plugin_description,
    author=plugin_author,
    url=plugin_url,
    license=plugin_license,
    packages=find_packages(),
    install_requires=plugin_requires + plugin_additional_packages,
    include_package_data=True,
    python_requires=">=2.7,<4",
    entry_points={
        "octoprint.plugin": [
            f"{plugin_identifier}={plugin_package}:__plugin_load__"
        ]
    }
)
