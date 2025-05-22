import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-21,0))
r=w0.sketch().segment((-100,-99),(35,-99)).segment((35,5)).segment((100,5)).segment((100,98)).segment((35,98)).segment((35,99)).segment((-100,99)).close().assemble().finalize().extrude(42)