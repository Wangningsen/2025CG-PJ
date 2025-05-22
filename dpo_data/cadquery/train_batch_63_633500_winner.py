import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,37,0))
w1=cq.Workplane('YZ',origin=(-93,0,0))
r=w0.sketch().segment((-54,-80),(12,-80)).segment((12,-56)).arc((50,7),(12,70)).segment((12,93)).segment((-54,93)).segment((-54,70)).arc((-92,7),(-54,-56)).close().assemble().finalize().extrude(63).union(w1.sketch().segment((-100,65),(-22,65)).segment((-22,92)).segment((-26,92)).segment((-26,77)).segment((-100,77)).close().assemble().push([(-61,71)]).circle(2,mode='s').finalize().extrude(2))