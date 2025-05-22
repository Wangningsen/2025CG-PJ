import cadquery as cq
w0=cq.Workplane('YZ',origin=(-91,0,0))
w1=cq.Workplane('ZX',origin=(0,37,0))
r=w0.sketch().segment((-100,65),(-33,65)).arc((-29,55),(-22,47)).segment((-26,92)).arc((-30,85),(-33,77)).segment((-100,77)).close().assemble().finalize().extrude(-2).union(w1.sketch().segment((-54,-80),(12,-80)).segment((12,-56)).arc((50,7),(12,70)).segment((12,93)).segment((-54,93)).segment((-54,70)).arc((-92,7),(-54,-56)).close().assemble().finalize().extrude(63))