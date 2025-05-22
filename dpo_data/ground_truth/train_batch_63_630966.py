import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,20))
r=w0.sketch().arc((-68,-20),(-85,-85),(-28,-48)).segment((-9,-48)).segment((-9,-18)).segment((-68,-18)).close().assemble().push([(-78,62.5)]).rect(40,59).push([(84,-67)]).rect(32,40).finalize().extrude(-39)