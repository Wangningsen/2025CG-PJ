import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-9))
r=w0.sketch().segment((-100,49),(-91,39)).segment((-91,98)).segment((-99,98)).segment((-99,51)).close().assemble().finalize().extrude(-65).union(w0.sketch().push([(58.5,-32.5)]).rect(83,131).push([(58,-33)]).circle(11,mode='s').finalize().extrude(84))