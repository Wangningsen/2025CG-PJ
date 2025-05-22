import cadquery as cq
w0=cq.Workplane('YZ',origin=(90,0,0))
r=w0.workplane(offset=-181/2).moveTo(-61,-65).cylinder(181,23).union(w0.sketch().push([(-80,89)]).circle(11).push([(55,-64)]).circle(36).finalize().extrude(-135))