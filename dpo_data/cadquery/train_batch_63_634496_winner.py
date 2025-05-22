import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,12,0))
r=w0.sketch().arc((85,76),(99,76),(88,72)).segment((92,72)).segment((92,79)).segment((85,79)).close().assemble().push([(97,81)]).circle(3,mode='s').finalize().extrude(-27).union(w0.workplane(offset=3/2).moveTo(-59,-60.5).box(82,53,3))