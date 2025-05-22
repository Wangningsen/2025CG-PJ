import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,20))
r=w0.sketch().arc((-65,-20),(-84,-86),(-29,-48)).segment((-9,-48)).segment((-9,-18)).segment((-65,-18)).close().assemble().push([(-78.5,63)]).rect(41,58).push([(84,-67)]).rect(32,40).finalize().extrude(-39)