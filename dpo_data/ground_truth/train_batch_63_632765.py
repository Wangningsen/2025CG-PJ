import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,12))
w1=cq.Workplane('XY',origin=(0,0,-25))
r=w0.sketch().segment((-93,-55),(-93,-54)).segment((-62,-54)).arc((-70,-37),(-71,-18)).arc((-94,-75),(-32,-77)).arc((-48,-68),(-61,-55)).close().assemble().push([(59,51)]).circle(41).finalize().extrude(19).union(w0.workplane(offset=38/2).moveTo(21,4.5).box(24,5,38)).union(w1.workplane(offset=-26/2).moveTo(66,1).cylinder(26,23))