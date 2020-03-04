from directory_manager import SMBManager


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

