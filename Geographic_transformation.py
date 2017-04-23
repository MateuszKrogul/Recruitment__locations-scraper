from pyproj import Proj, transform
def G_transform(x1,y1):
    inProj = Proj(init='epsg:2177')
    outProj = Proj(proj='latlong')
    y2, x2 = transform(inProj, outProj, x1, y1)
    return x2,y2