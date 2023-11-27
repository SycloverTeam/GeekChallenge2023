import PIL.Image 
from hilbertcurve.hilbertcurve import HilbertCurve 
p,n = 256,2 
ct = PIL.Image.open(r'ct.png').convert('RGB') 
print(ct.width,ct.height)

pt = PIL.Image.new('RGB',(p,p))
print('step2')
hilbert_curve = HilbertCurve(p,n) 
distances = list(range(p**2)) 
points = hilbert_curve.points_from_distances(distances) 
print('step3') 
for point, dist in zip(points, distances): 
    x,y = point  
    print(x,y)
    pix = ct.getpixel((0,dist)) 
    pt.putpixel((x,y),pix) 

pt.save(r'pt1.png')