import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-1))
w1=cq.Workplane('ZX',origin=(0,33,0))
r=w0.sketch().segment((-14,6),(7,6)).segment((7,16)).arc((12,29),(7,42)).segment((7,51)).segment((-1,51)).segment((-1,42)).arc((-7,36),(-8,28)).segment((-14,28)).close().assemble().finalize().extrude(-21).union(w0.sketch().push([(-65.5,26.5)]).rect(69,1).push([(63.5,10)]).rect(73,28).finalize().extrude(-13)).union(w1.workplane(offset=-85/2).moveTo(1,-2).cylinder(85,21))