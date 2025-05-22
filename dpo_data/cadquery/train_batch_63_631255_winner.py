import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-27,0))
r=w0.sketch().push([(-5.5,-14)]).rect(61,84).push([(-6,-14)]).circle(1,mode='s').finalize().extrude(-5).union(w0.workplane(offset=38/2).moveTo(69.5,90.5).box(5,19,38)).union(w0.sketch().segment((-72,-99),(-69,-100)).segment((-63,-70)).segment((-66,-70)).close().assemble().push([(20,5.5)]).rect(50,79).finalize().extrude(59))