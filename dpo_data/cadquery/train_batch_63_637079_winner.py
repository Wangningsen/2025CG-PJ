import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,49,0))
r=w0.sketch().segment((-100,-25),(-65,-80)).segment((100,25)).segment((65,80)).close().assemble().circle(18,mode='s').finalize().extrude(-98)