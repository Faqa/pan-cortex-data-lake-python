# -*- coding: utf-8 -*-

"""Base adapter class."""
from __future__ import absolute_import

from abc import ABCMeta, abstractmethod

# Python 2.7 and 3.5+ compatibility
ABC = ABCMeta('ABC', (object,), {'__slots__': ()})


class StorageAdapter(ABC):  # enforce StorageAdapter interface
    """A storage adapter abstract base class."""

    @abstractmethod
    def fetch_credential(self, credential=None, profile=None):
        """Fetch credential from store.

        Args:
            credential (str): Credential to fetch.
            profile (str): Credentials profile. Defaults to ``'default'``.

        Returns:
            str, None: Fetched credential or ``None``.

        """
        pass

    @abstractmethod
    def init_store(self):
        """Initialize credentials store."""
        pass

    @abstractmethod
    def remove_profile(self, profile=None):
        """Remove profile from store.

        Args:
            profile (str): Credentials profile to remove.

        Returns:
            int: Result of operation.

        """
        pass

    @abstractmethod
    def write_credentials(self, credentials=None, profile=None):
        """Write credentials.

        Write credentials to store.

        Args:
            credentials (class): Read-only credentials.
            profile (str): Credentials profile. Defaults to ``'default'``.

        Returns:
            int: Result of operation.

        """
        pass
