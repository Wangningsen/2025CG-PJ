import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,100,0))
r=w0.sketch().segment((-50,-11),(-8,-11)).segment((-8,-92)).segment((14,-92)).segment((14,-11)).segment((50,-11)).segment((50,47)).segment((14,47)).segment((14,92)).segment((-8,92)).segment((-8,47)).segment((-50,47)).close().assemble().finalize().extrude(-200)