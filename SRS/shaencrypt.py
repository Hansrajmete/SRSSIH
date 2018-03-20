import hashlib
import time

def encrypt_string(format_iso_now):

    hash_string="SRSfPxIFCoUJMH3HPBB10Eo"+format_iso_now
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()

    return sha_signature