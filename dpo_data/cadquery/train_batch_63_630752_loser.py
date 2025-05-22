import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,65,0))
r=w0.sketch().segment((-55,88),(-48,74)).segment((-22,87)).segment((-29,100)).close().assemble().reset().face(w0.sketch().segment((22,-87),(29,-100)).segment((55,-88)).segment((48,-74)).close().assemble()).finalize().extrude(-130).union(w0.sketch().circle(48).circle(4,mode='s').finalize().extrude(-117))