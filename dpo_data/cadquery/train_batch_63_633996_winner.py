import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-47,0))
r=w0.sketch().segment((-100,-32),(-44,-48)).segment((-44,-59)).segment((-29,-59)).arc((52,-58),(61,19)).segment((66,34)).segment((100,34)).segment((100,59)).segment((16,59)).segment((16,50)).segment((12,48)).segment((11,48)).segment((11,62)).segment((-30,62)).segment((-71,74)).close().assemble().finalize().extrude(94)