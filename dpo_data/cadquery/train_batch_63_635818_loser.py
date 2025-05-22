import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,49,0))
r=w0.sketch().segment((-33,4),(57,-69)).segment((100,-16)).segment((63,14)).arc((56,26),(44,35)).segment((-6,69)).segment((-32,37)).arc((-100,24),(-33,4)).assemble().finalize().extrude(-99)