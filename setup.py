#!/usr/bin/env python
"""
Example plugin for MultiQC, showing how to structure code
and plugin hooks to work effectively with the main MultiQC code.

For more information about MultiQC, see http://multiqc.info
"""

from setuptools import setup, find_packages

version = "0.3"

setup(
    name="multiqc_mgikit_plugin",
    version=version,
    author="Ziad Al Bkhetan",
    author_email="",
    description="MGIKIT MultiQC plugin",
    long_description=__doc__,
    keywords="bioinformatics",
    url="",
    download_url="",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["multiqc"],
    entry_points={
        "multiqc.modules.v1": [
            "mgikit = mgikit.modules.mgikit:MultiqcModule",
        ],
        "multiqc.cli_options.v1": ["disable_plugin = mgikit.cli:disable_plugin",
                                   "undetermined_barcode_threshold = mgikit.cli:undetermined_barcode_threshold",
                                   "brief_report = mgikit.cli:brief_report",
                                   "keep_core_samples = mgikit.cli:keep_core_samples",
                                   "decimal_positions = mgikit.cli:decimal_positions"],
        "multiqc.hooks.v1": [
            "execution_start = mgikit.custom_code:mgikit_plugin_execution_start"
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Programming Language :: Python",
        "Programming Language :: JavaScript",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Scientific/Engineering :: Visualization",
    ],
)
