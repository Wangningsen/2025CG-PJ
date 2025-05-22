import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-9,0))
r=w0.sketch().push([(0,-26)]).circle(74).push([(0,-25.5)]).rect(38,119,mode='s').finalize().extrude(-57).union(w0.sketch().segment((-37,87),(52,35)).segment((59,48)).segment((-30,100)).close().assemble().finalize().extrude(76))