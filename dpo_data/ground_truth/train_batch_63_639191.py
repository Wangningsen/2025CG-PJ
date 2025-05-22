import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-48,0))
r=w0.sketch().segment((-100,41),(-74,-54)).segment((-42,-45)).segment((-41,-7)).segment((-39,-7)).segment((-56,54)).close().assemble().push([(81.5,8)]).rect(37,46).finalize().extrude(96)