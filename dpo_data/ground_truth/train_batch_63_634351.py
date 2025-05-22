import cadquery as cq
w0=cq.Workplane('YZ',origin=(-31,0,0))
r=w0.sketch().push([(-37.5,-47)]).rect(59,106).push([(-40,89)]).circle(11).finalize().extrude(49).union(w0.workplane(offset=63/2).moveTo(40,-37.5).box(54,105,63))