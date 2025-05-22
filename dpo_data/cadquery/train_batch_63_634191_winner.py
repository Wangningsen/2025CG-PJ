import cadquery as cq
w0=cq.Workplane('YZ',origin=(-100,0,0))
r=w0.sketch().segment((-51,-15),(51,-15)).segment((23,11)).segment((26,15)).segment((-51,15)).close().assemble().finalize().extrude(200)