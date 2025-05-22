import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-42))
r=w0.workplane(offset=10/2).moveTo(-40,-55).cylinder(10,45).union(w0.workplane(offset=50/2).moveTo(-33,8).cylinder(50,10)).union(w0.sketch().segment((0,69),(59,20)).segment((85,51)).segment((26,100)).close().assemble().push([(17.5,-57.5)]).rect(11,67).finalize().extrude(84))