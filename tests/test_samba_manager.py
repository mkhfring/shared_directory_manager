import os

import pytest

from directory_manager import SMBManager
from directory_manager.exceptions import ConnectionException


def test_samba_manager():
    smb_manager = SMBManager(
        '192.168.15.135',
        'kiosktest',
        'Kss@1$ba',
        'kioskshare'
    )
    shared_directories = smb_manager._list_shared_directories()
    assert shared_directories is not None
    assert smb_manager.get_shared_directory == 'KioskShare'

def test_samba_connection_error():
    smb_manager = SMBManager(
        '192.168.15.135',
        'kiosktest',
        'Wrongpass',
        'kioskshare'
    )
    with pytest.raises(ConnectionException):
        smb_manager._connect()

def test_samba_manager_get_file():
    smb_manager = SMBManager(
        '192.168.15.135',
        'kiosktest',
        'Kss@1$ba',
        'kioskshare'
    )
    file_attr, file_size = smb_manager.get_file(
        'f.jpg',
        'tests/data/flower.jpg'
    )
    assert file_attr is not None
    assert file_size is not None
    assert os.path.exists('tests/data/flower.jpg')
    os.remove('tests/data/flower.jpg')

def test_samba_manager_put_file():
    smb_manager = SMBManager(
        '192.168.15.135',
        'kiosktest',
        'Kss@1$ba',
        'kioskshare'
    )
    file_size = smb_manager.put_file(
       'tests/data/f.jpg',
       'flower.jpg'
    )
    assert file_size is not None

