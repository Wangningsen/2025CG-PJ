import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,64,0))
r=w0.sketch().segment((-100,-89),(-74,-89)).segment((-76,-98)).segment((-69,-99)).segment((-64,-74)).arc((-68,-75),(-70,-73)).segment((-74,-88)).arc((-86,-69),(-71,-51)).segment((-100,-51)).close().assemble().finalize().extrude(-128).union(w0.sketch().arc((68,98),(21,41),(95,41)).arc((96,76),(68,98)).assemble().finalize().extrude(-5))