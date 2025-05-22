import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-18,0))
r=w0.sketch().segment((-88,-74),(-58,-81)).segment((-58,-100)).segment((-33,-100)).segment((-33,-87)).segment((-5,-93)).segment((-3,-82)).segment((-33,-75)).segment((-33,-57)).segment((-58,-57)).segment((-58,-70)).segment((-86,-63)).close().assemble().push([(29,65.5)]).rect(118,69).finalize().extrude(36)