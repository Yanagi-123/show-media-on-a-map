# encoding: UTF-8

from PIL import Image
from PIL.ExifTags import TAGS


class ExifTag:

    def __init__(self):

        self.gps_info = None

    def get_exif(self, image):
        # PIL.JpegImagePlugin.JpegImageFile
        try:
            exif = image._getexif()
        except AttributeError:
            exif = {}

        exif_table = {}
        for tag_id, value in exif.items():
            tag = TAGS.get(tag_id, tag_id)
            exif_table[tag] = value

        if "GPSInfo" in exif_table:
            self.gps_info = exif_table["GPSInfo"]

    def location_to_gps(self):



if __name__ == '__main__':
    exif = ExifTag()
    i = Image.open("sample.jpg")
    exif.get_exif(i)
    print(exif.gps_info)
