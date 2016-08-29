import sys
import getopt

from PIL import Image

formatters = {
    'RED': '\033[91m',
    'GREEN': '\033[92m',
    'END': '\033[0m',
}


def main(input_path, argv):
    output_name = "example_new"
    height = 1200
    width = 1200
    try:
        opts, args = getopt.getopt(argv, "h:w:o:", ["height=", "width=", "output="])
    except getopt.GetoptError:
        print "Usage: resize_image.py image_path -o <output_name> -h <height> -w <width>"
        sys.exit(2)

    for opt, arg in opts:
        if opt == "--help":
            print "Usage: resize_image.py image_path -o <output_name> -h <height> -w <width>"
            sys.exit()

        if opt in ("-o", "--output"):
            output_name = arg
        if opt in ("-h", "--height"):
            height = arg
        if opt in ("-w", "--width"):
            width = arg

    resize_image(input_path, output_name=output_name, height=height, width=width)


def resize_image(image_path, output_name="example_new", height=1200, width=1200):
    """
    Re-sizing given image with a ratio of
    given width and height
    """
    print "{GREEN}Processing...{END}".format(**formatters)    
    image = Image.open(image_path)
    print image_path
    image.thumbnail((int(height), int(width)), Image.ANTIALIAS)
    print "%s.%s" % (output_name, image_path.split(".")[-1])
    image.save("%s.%s" % (output_name, image_path.split(".")[-1]))
    print "{GREEN}Finished.{END}".format(**formatters)    

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1]:
        main(sys.argv[1], sys.argv[2:])
    else:
        print "{RED}Please provide image path!{END}".format(**formatters)
        print "Usage: resize_image.py image_path -o <output_name> -h <height> -w <width>"
