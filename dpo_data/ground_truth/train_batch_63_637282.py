import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,32))
r=w0.sketch().push([(-42,-10)]).circle(16).push([(28.5,26)]).rect(77,18).push([(4,-16)]).circle(13).finalize().extrude(-132).union(w0.sketch().arc((-33,-33),(-36,-14),(-18,-6)).arc((-64,2),(-33,-33)).assemble().finalize().extrude(68))