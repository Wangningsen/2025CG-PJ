import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-12,0))
r=w0.workplane(offset=-72/2).moveTo(-87,-15).cylinder(72,9).union(w0.workplane(offset=46/2).moveTo(-60.5,-36.5).box(79,51,46)).union(w0.sketch().segment((-96,-68),(-84,-68)).segment((-84,-35)).segment((-25,-35)).segment((-25,-6)).segment((-96,-6)).close().assemble().push([(63,16.5)]).rect(74,103).finalize().extrude(96))