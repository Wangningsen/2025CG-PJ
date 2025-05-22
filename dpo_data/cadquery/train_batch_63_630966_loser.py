import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,20))
r=w0.sketch().arc((-61,-18),(-90,-81),(-27,-48)).segment((-9,-48)).segment((-9,-18)).close().assemble().push([(-78.5,62.5)]).rect(41,59).push([(84,-67)]).rect(32,40).finalize().extrude(-39)