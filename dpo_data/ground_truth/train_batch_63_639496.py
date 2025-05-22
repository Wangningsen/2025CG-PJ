import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,3,0))
w1=cq.Workplane('XY',origin=(0,0,-19))
r=w0.sketch().push([(-15.5,-81.5)]).rect(15,37).push([(-18.5,-98)]).rect(3,4,mode='s').finalize().extrude(16).union(w0.workplane(offset=43/2).moveTo(-1.5,-43).box(79,10,43)).union(w1.sketch().segment((-26,-73),(47,-73)).segment((47,-24)).segment((100,-24)).segment((100,73)).segment((2,73)).segment((2,7)).segment((-26,7)).close().assemble().finalize().extrude(60))