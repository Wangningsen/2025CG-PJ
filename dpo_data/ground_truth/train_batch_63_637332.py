import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,42,0))
r=w0.sketch().arc((-84,-9),(-60,-80),(-39,-8)).arc((-61,-18),(-84,-9)).assemble().push([(52.5,48.5)]).rect(95,63).finalize().extrude(-84)