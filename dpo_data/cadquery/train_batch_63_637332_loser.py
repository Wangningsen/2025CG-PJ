import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,42,0))
r=w0.sketch().arc((-85,-10),(-56,-79),(-40,-8)).arc((-62,-18),(-85,-10)).assemble().push([(52.5,48.5)]).rect(95,63).finalize().extrude(-84)