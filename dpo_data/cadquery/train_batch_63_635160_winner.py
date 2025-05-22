import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,15))
r=w0.workplane(offset=-115/2).moveTo(-85,-7).cylinder(115,6).union(w0.workplane(offset=-32/2).moveTo(24.5,-57).box(93,54,32)).union(w0.sketch().push([(-44,33)]).circle(20).push([(35,28)]).circle(56).finalize().extrude(85))