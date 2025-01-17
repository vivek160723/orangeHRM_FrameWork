import pytest

# This hook is triggered when pytest configures the tests
def pytest_configure(config):
    # No metadata modification, just configuring the tests
    pass

# This hook removes unnecessary metadata from the report
def pytest_metadata(metadata):
    # Remove unnecessary metadata fields
    metadata.pop('Plugins', None)
    metadata.pop('Platform', None)
