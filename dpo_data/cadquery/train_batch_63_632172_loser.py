import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,29,0))
r=w0.sketch().push([(7,-23.5)]).rect(10,19).push([(7,-24)]).circle(1,mode='s').finalize().extrude(-57).union(w0.sketch().push([(-65,-53)]).rect(70,8).reset().face(w0.sketch().segment((-45,-35),(-41,-36)).segment((-41,-10)).arc((-27,56),(-45,-9)).close().assemble()).push([(72,-21)]).circle(28).finalize().extrude(-52))