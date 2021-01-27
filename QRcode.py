import qrcode

def make_qr(data, name):
	qr = qrcode.QRCode(
		version=1,
		box_size=5,
		border=5
		)

	qr.add_data(data)
	qr.make(fit=True)

	img = qr.make_image(fill='black', back_color='white', )

	img.save(f'QRCodes/{name}.png')

