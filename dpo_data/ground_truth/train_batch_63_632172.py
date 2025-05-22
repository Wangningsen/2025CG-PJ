import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,28,0))
r=w0.sketch().push([(7,-23)]).rect(10,20).push([(7,-16.5)]).rect(8,5,mode='s').finalize().extrude(-57).union(w0.sketch().push([(-65,-52.5)]).rect(70,9).reset().face(w0.sketch().segment((-45,-35),(-41,-35)).segment((-41,-9)).arc((-24,56),(-45,-8)).close().assemble()).push([(72,-21)]).circle(28).finalize().extrude(-51))