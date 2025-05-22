import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-26,0))
r=w0.sketch().push([(22,85)]).circle(15).circle(9,mode='s').finalize().extrude(28).union(w0.workplane(offset=32/2).moveTo(54.5,46.5).box(35,9,32)).union(w0.sketch().segment((-72,-99),(-65,-100)).segment((-56,-49)).segment((-63,-48)).close().assemble().push([(-64,-74)]).circle(4,mode='s').finalize().extrude(53))