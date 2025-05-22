import cadquery as cq
w0=cq.Workplane('YZ',origin=(3,0,0))
r=w0.sketch().segment((-84,-66),(-42,-100)).segment((84,63)).segment((36,100)).segment((-59,-23)).segment((-54,-42)).segment((-59,-43)).segment((-62,-50)).segment((-63,-50)).segment((-65,-52)).segment((-66,-50)).close().assemble().finalize().extrude(-6)