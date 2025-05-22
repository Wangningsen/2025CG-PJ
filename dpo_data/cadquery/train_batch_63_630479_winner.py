import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,57))
w1=cq.Workplane('XY',origin=(0,0,24))
r=w0.sketch().segment((52,-42),(78,-42)).segment((78,3)).arc((94,29),(78,55)).segment((78,100)).segment((52,100)).segment((52,55)).arc((36,29),(52,3)).close().assemble().push([(65,29)]).rect(8,22,mode='s').finalize().extrude(-123).union(w0.sketch().segment((-94,22),(-60,22)).arc((-60,25),(-61,28)).segment((-94,28)).close().assemble().finalize().extrude(-29)).union(w1.sketch().push([(-40,-64.5)]).rect(38,71).push([(-32.5,-48.5)]).rect(7,19,mode='s').finalize().extrude(42))