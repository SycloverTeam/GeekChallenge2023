from PIL import Image

def mk_png2bit(filename, length):
    pic = Image.open(filename)
    pic.convert('1')
    bit = []
    for y in range(length):
        for x in range(length):
            bit.append(0 if pic.getpixel((x, y))[0] == 255 else 1)
    return bit

def mk_bit2png(filename, length, bit):
    pic = Image.new("RGB",(length, length))
    i=0
    for y in range (length):
        for x in range (length):
            if(bit[i] == 1):
                pic.putpixel([x,y],(0, 0, 0))
            else:
                pic.putpixel([x,y],(255,255,255))
            i+=1
    pic.save(filename)

flag_bit = mk_png2bit("qr_code_syc_hop3.png", 25)
xor_bit = mk_png2bit("qr_code_syc_this.png", 25)

for i in range(625):
    xor_bit[i]^=flag_bit[i]

mk_bit2png("out.png", 25, xor_bit)