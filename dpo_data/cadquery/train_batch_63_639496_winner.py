import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-19))
w1=cq.Workplane('ZX',origin=(0,46,0))
r=w0.workplane(offset=11/2).moveTo(-82,11).box(36,16,11).union(w0.sketch().segment((-26,-73),(47,-73)).segment((47,-24)).segment((100,-24)).segment((100,73)).segment((2,73)).segment((2,7)).segment((-26,7)).close().assemble().finalize().extrude(60)).union(w1.workplane(offset=-43/2).moveTo(-1.5,-43).box(79,10,43))