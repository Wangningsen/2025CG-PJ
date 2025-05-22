import cadquery as cq
w0=cq.Workplane('YZ',origin=(28,0,0))
w1=cq.Workplane('XY',origin=(0,0,33))
r=w0.sketch().push([(-63,17)]).circle(37).push([(43.5,-11.5)]).rect(47,97).finalize().extrude(-112).union(w0.workplane(offset=57/2).moveTo(43,-12).cylinder(57,57)).union(w1.workplane(offset=35/2).moveTo(11.5,43.5).box(21,29,35))