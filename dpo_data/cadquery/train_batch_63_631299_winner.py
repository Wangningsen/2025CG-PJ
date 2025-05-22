import cadquery as cq
w0=cq.Workplane('YZ',origin=(-6,0,0))
r=w0.sketch().segment((-77,74),(-40,74)).segment((-42,100)).segment((-77,100)).close().assemble().finalize().extrude(-89).union(w0.sketch().push([(31,-54)]).circle(46).push([(30.5,-54)]).rect(47,4,mode='s').finalize().extrude(100))