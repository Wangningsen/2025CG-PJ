import cadquery as cq
w0=cq.Workplane('YZ',origin=(-46,0,0))
r=w0.sketch().segment((-100,-57),(24,-57)).arc((64,-72),(47,-33)).segment((47,46)).segment((45,46)).segment((45,-33)).arc((34,-37),(26,-46)).segment((26,-11)).segment((-100,-11)).close().assemble().push([(89.5,58.5)]).rect(21,41).finalize().extrude(91).union(w0.workplane(offset=93/2).moveTo(46,-1).box(2,24,93))