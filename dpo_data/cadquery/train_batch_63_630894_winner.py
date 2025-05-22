import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,23,0))
w1=cq.Workplane('XY',origin=(0,0,57))
r=w0.sketch().segment((51,-87),(62,-87)).segment((62,-76)).segment((51,-76)).segment((51,-81)).segment((52,-81)).segment((52,-83)).segment((51,-83)).close().assemble().push([(94.5,-81.5)]).rect(11,11).finalize().extrude(-78).union(w1.workplane(offset=-157/2).moveTo(11.5,36.5).box(151,37,157))