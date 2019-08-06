import unittest


class TestCoincurve(unittest.TestCase):

    # From https://github.com/ofek/coincurve/tree/master/tests
    def test_basic(self):
        from coincurve import verify_signature

        public_key = (
            b"\x03=\\(u\xc9\xbd\x11hu\xa7\x1a]\xb6L\xff\xcb\x139k\x16=\x03\x9b"
            b"\x1d\x93'\x82H\x91\x80C4")
        message = (
            b'\xdfw\xeb)\t2R8\xda5\x02\xadE\xdd\xce\xd2\xe0\xb4\xf1\x81\xe7\xdf'
            b':\xce\x82m\xcf\x99\xf3o\x9d\xe6\xfb\xe4\x98O\x88\xcfh\xbe\xfd\xc2'
            b'{\xafm\xb3\xff\xb4QR\xffPu$\xfc>A\'\x03t\xc5\xf9\xd8\xf3I,\xaa"*'
            b'\xd7q\xfe\xb7]\x11\xa9uB\'d\x89\x03\'3\xb8/\x80\xa2#\x00\xa2\xfe'
            b'\xff\xae\xb0\x86\xc1/ o\xc8]?\xa05L\xff8\x8az\x92\xc9\xab\x9fg0|'
            b'\\5\x98\xfaG\x9b#\xec\x1a\xc5\x10\xd6\x08\x9c:\x01"\x0c\x812O/i'
            b'\xc4WI\x0c\r\xd8\x81-m1_\x14]$\xf8\x16\xef\x1e\x1d\xb0"Q\x1a\xcf'
            b'`R\xae\x0c"r2\x9a\xa3\xdb\xc4W}<c\xd8\x0e\xb5\x96\x99\x87\xdeU'
            b'\x84\x1a?No\x10T\xf8\xb8\xd3\x18\xa4\xaf')
        signature = (
            b"0E\x02!\x00\xee$\x1b\x0e@fa\xd4<\x17)\xa7\n\xd0\xd7\xef\x90\xcd\x13"
            b"\xad`\xc1\x06[\xe0\x821\x96\xe29\x80'\x02 \r\x02\x13\xd2\xaf?\x92G"
            b"\x80&8\x1cVz%2\xb0\x8a\xd0l\x0b4\x9c~\x93\x18\xad\xe4J\x9c-\n")

        self.assertTrue(verify_signature(signature, message, public_key))
        bad_message = b"\x00" + message[1:]
        self.assertFalse(verify_signature(signature, bad_message, public_key))
