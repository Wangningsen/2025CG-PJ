import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-55,0))
w1=cq.Workplane('XY',origin=(0,0,-36))
r=w0.workplane(offset=-35/2).moveTo(-48,-11).cylinder(35,52).union(w0.sketch().arc((-4,39),(-33,-62),(63,-33)).segment((35,-45)).segment((28,-30)).segment((48,-21)).segment((54,-32)).arc((56,-33),(58,-33)).segment((100,-33)).segment((100,-10)).segment((37,-10)).arc((25,28),(-4,39)).assemble().finalize().extrude(-22)).union(w1.sketch().arc((13,67),(-12,27),(33,13)).arc((94,63),(13,67)).assemble().push([(53,48)]).circle(34,mode='s').finalize().extrude(11))