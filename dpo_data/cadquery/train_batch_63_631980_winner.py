import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-12,0))
r=w0.sketch().segment((-50,-61),(4,-61)).segment((4,-82)).segment((15,-66)).segment((-30,-32)).segment((-40,-45)).arc((-96,-20),(-50,-61)).assemble().push([(92,52.5)]).rect(16,59).finalize().extrude(24)