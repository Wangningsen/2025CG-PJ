import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-29))
w1=cq.Workplane('XY',origin=(0,0,-43))
r=w0.sketch().push([(-73,-45)]).circle(27).push([(-73.5,13)]).rect(9,48).push([(8,-14)]).circle(27).finalize().extrude(72).union(w1.sketch().segment((-32,6),(32,6)).segment((32,-38)).segment((68,-38)).segment((68,-57)).segment((100,-57)).segment((100,21)).segment((90,21)).segment((90,31)).segment((32,31)).segment((32,72)).segment((-32,72)).close().assemble().finalize().extrude(74))