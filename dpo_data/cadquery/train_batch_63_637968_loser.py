import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-42))
r=w0.sketch().push([(-41,-55)]).circle(45).push([(-33,7)]).circle(11).finalize().extrude(10).union(w0.workplane(offset=49/2).moveTo(-33,7).cylinder(49,11)).union(w0.sketch().segment((0,69),(59,20)).segment((85,51)).segment((25,100)).close().assemble().push([(17.5,-57.5)]).rect(11,67).finalize().extrude(84))