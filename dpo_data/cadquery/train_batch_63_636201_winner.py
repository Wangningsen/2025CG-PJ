import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,64,0))
r=w0.sketch().segment((-100,-89),(-74,-89)).segment((-76,-98)).segment((-69,-100)).segment((-64,-75)).segment((-72,-73)).segment((-76,-88)).arc((-86,-69),(-71,-51)).segment((-100,-51)).close().assemble().finalize().extrude(-128).union(w0.sketch().push([(59,58)]).circle(41).circle(1,mode='s').finalize().extrude(-5))