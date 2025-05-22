import cadquery as cq
w0=cq.Workplane('YZ',origin=(38,0,0))
w1=cq.Workplane('YZ',origin=(46,0,0))
r=w0.sketch().push([(33,69)]).circle(31).circle(18,mode='s').push([(56,96)]).circle(2).finalize().extrude(-97).union(w0.sketch().segment((-94,-75),(-93,-98)).segment((-76,-97)).segment((-76,-63)).segment((-94,-63)).segment((-94,-74)).segment((-92,-72)).segment((-92,-66)).segment((-86,-66)).segment((-86,-72)).segment((-90,-72)).segment((-87,-74)).segment((-91,-78)).close().assemble().finalize().extrude(21)).union(w1.workplane(offset=-85/2).moveTo(57,-63).cylinder(85,37))