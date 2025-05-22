import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-29))
w1=cq.Workplane('XY',origin=(0,0,-43))
r=w0.sketch().push([(-73,-45)]).circle(27).push([(-73.5,12.5)]).rect(9,49).push([(8,-13)]).circle(28).finalize().extrude(72).union(w1.sketch().segment((-32,6),(32,6)).segment((32,-38)).segment((68,-38)).segment((68,-57)).segment((100,-57)).segment((100,21)).segment((84,21)).segment((84,31)).segment((32,31)).segment((32,72)).segment((-32,72)).close().assemble().finalize().extrude(74))