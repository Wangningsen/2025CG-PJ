import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,48,0))
r=w0.sketch().segment((-100,-20),(-75,-20)).segment((-65,-59)).segment((-36,-52)).segment((-44,-20)).segment((-21,-20)).segment((-21,-7)).segment((-47,-7)).segment((-56,32)).segment((-85,25)).segment((-78,-7)).segment((-100,-7)).close().assemble().push([(52,11)]).circle(48).finalize().extrude(-96)