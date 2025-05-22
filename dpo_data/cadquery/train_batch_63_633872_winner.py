import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-27))
r=w0.sketch().arc((-75,-8),(13,-22),(-67,14)).arc((-99,12),(-75,-8)).assemble().finalize().extrude(-33).union(w0.sketch().push([(56,-23.5)]).rect(88,93).push([(57,60)]).circle(10).finalize().extrude(87))