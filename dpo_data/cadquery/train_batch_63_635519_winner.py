import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-23,0))
w1=cq.Workplane('XY',origin=(0,0,10))
r=w0.sketch().segment((-29,8),(-27,4)).segment((20,8)).close().assemble().finalize().extrude(78).union(w0.sketch().push([(-50.5,-18.5)]).rect(99,11).push([(26,50.5)]).rect(14,3).push([(78,50.5)]).rect(14,3).finalize().extrude(79)).union(w1.workplane(offset=90/2).moveTo(-19.5,-52.5).box(65,7,90))