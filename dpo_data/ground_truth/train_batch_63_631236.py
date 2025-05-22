import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,31))
r=w0.sketch().arc((-92,-9),(-63,-79),(-9,-26)).segment((-34,-57)).segment((-73,-25)).segment((-25,17)).segment((-33,26)).segment((-82,-17)).close().assemble().push([(50,22)]).rect(100,116).finalize().extrude(-61)