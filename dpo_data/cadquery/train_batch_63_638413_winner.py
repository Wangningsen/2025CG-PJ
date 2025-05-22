import cadquery as cq
w0=cq.Workplane('YZ',origin=(-2,0,0))
r=w0.sketch().arc((-17,-2),(0,-100),(17,-2)).arc((0,100),(-17,-2)).assemble().finalize().extrude(4)