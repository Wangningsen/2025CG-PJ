import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-69,0))
r=w0.sketch().segment((-53,88),(-25,-100)).segment((53,-88)).segment((25,100)).close().assemble().circle(25,mode='s').finalize().extrude(139)