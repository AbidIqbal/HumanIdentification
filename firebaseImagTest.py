from PIL import Image
from google.cloud import storage

client = storage.Client()
bucket = client.get_bucket('fypapplication-22974.appspot.com')
blob = bucket.blob('c3.jpg')
# use pillow to open and transform the file
# image = Image.open(file)
# # perform transforms
# outfile='kim.jpg'
# image.save(outfile)
# of = open(outfile, 'rb')
# blob.upload_from_file(of)
# # or... (no need to use pillow if you're not transforming)
# blob.upload_from_filename()