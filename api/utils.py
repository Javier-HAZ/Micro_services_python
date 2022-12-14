import hashlib
import os
import imghdr

def allowed_file(filename):
    """
    Checks if the format for the file received is acceptable. For this
    particular case, we must accept only image files. This is, files with
    extension ".png", ".jpg", ".jpeg" or ".gif".

    Parameters
    ----------
    filename : str
        Filename from werkzeug.datastructures.FileStorage file.

    Returns
    -------
    bool
        True if the file is an image, False otherwise.
    """
    # Current implementation will allow any kind of file.
    # TODO
    file_format = imghdr.what(filename)
    valid_extns = ["png", "jpg", "jpeg", "gif"]
    valid = file_format in valid_extns

    return valid

def get_file_hash(file):
    """
    Returns a new filename based on the file content using MD5 hashing.
    It uses hashlib.md5() function from Python standard library to get
    the hash.

    Parameters
    ----------
    file : werkzeug.datastructures.FileStorage
        File sent by user.

    Returns
    -------
    str
        New filename based in md5 file hash.
    """
    # Current implementation will return the original file name.
    # TODO
    filename = os.path.basename(file.filename)
    hash_obj = hashlib.md5(bytes(filename, "utf8"))
    hash_encode = hash_obj.digest()
    hash_name = filename + "_" + hash_encode.split("'")[1]

    return hash_name
