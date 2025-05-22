import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,50,0))
r=w0.sketch().arc((-7,39),(-95,-52),(18,-84)).arc((-19,-24),(68,-29)).arc((96,10),(93,59)).segment((93,55)).segment((84,55)).segment((84,65)).segment((88,65)).arc((46,98),(-5,92)).arc((2,64),(-7,39)).assemble().finalize().extrude(-100)