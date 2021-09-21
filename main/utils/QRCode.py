import qrcode
import time

from main.utils import FileOP

def getQRCode(word: str, 
              autoRemove: bool=True, 
              version: int=2, 
              error_correction=qrcode.ERROR_CORRECT_H, 
              box_size: int=10, 
              border: int=4, 
              mask_pattern=None) -> bytes:

    qr = qrcode.QRCode(
        version=version,
        error_correction=error_correction,
        box_size=box_size,
        border=border,
        mask_pattern=mask_pattern
    )

    qr.add_data(word)
    qr.make()
    img = qr.make_image(fill_color="black", back_color="white")

    tempFile = str(round(time.time())) + ".png"
    tempFile = FileOP.setTemp(tempFile)

    stream = None
    with open(tempFile, "wb") as f:
        img.save(f)
    with open(tempFile, "rb") as f:
        stream = f.read()
    
    if autoRemove:
        FileOP.removeFile(tempFile)
    
    return stream


