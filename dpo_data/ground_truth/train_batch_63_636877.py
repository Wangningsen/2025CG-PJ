import cadquery as cq
w0=cq.Workplane('YZ',origin=(61,0,0))
r=w0.sketch().push([(-54,-69.5)]).rect(82,61).push([(-54,-70)]).circle(27,mode='s').finalize().extrude(-123).union(w0.sketch().segment((-17,69),(2,11)).segment((95,42)).segment((75,100)).close().assemble().push([(39,55)]).circle(8,mode='s').finalize().extrude(-97))