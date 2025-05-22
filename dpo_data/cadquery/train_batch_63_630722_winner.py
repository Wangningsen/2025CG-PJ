import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,47))
r=w0.sketch().push([(-66,-11)]).circle(34).push([(-69,-0.5)]).rect(30,33,mode='s').push([(-50.5,-24.5)]).rect(23,7,mode='s').finalize().extrude(-118).union(w0.sketch().segment((-94,-22),(-79,-22)).arc((95,30),(-82,4)).segment((-94,4)).close().assemble().finalize().extrude(24))