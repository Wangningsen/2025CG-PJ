import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,25,0))
r=w0.sketch().segment((-12,37),(28,37)).arc((44,33),(60,37)).segment((100,37)).segment((100,94)).segment((60,94)).arc((44,98),(28,94)).segment((-12,94)).close().assemble().finalize().extrude(-99).union(w0.sketch().push([(-90,-88)]).circle(10).push([(-89.5,-88)]).rect(19,8,mode='s').finalize().extrude(48))