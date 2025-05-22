import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-20,0))
w1=cq.Workplane('XY',origin=(0,0,53))
r=w0.sketch().push([(-12,60)]).rect(96,80).reset().face(w0.sketch().segment((-53,54),(-20,54)).segment((-20,48)).segment((-4,48)).segment((-4,54)).segment((29,54)).segment((29,66)).segment((-4,66)).segment((-4,72)).segment((-20,72)).segment((-20,66)).segment((-53,66)).close().assemble(),mode='s').push([(59,-91.5)]).rect(2,17).finalize().extrude(82).union(w1.workplane(offset=-94/2).moveTo(-91.5,-36.5).box(17,49,94))