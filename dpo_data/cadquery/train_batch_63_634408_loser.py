import cadquery as cq
w0=cq.Workplane('YZ',origin=(-83,0,0))
w1=cq.Workplane('ZX',origin=(0,-21,0))
r=w0.sketch().push([(-37,6)]).rect(48,94).push([(21.5,59)]).rect(81,2).finalize().extrude(-17).union(w1.sketch().push([(-12,60)]).rect(96,80).reset().face(w1.sketch().segment((-53,54),(-20,54)).segment((-20,48)).segment((-4,48)).segment((-4,54)).segment((29,54)).segment((29,66)).segment((-4,66)).segment((-4,72)).segment((-20,72)).segment((-20,66)).segment((-53,66)).close().assemble(),mode='s').finalize().extrude(82))