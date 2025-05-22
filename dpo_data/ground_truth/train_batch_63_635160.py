import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,15))
r=w0.sketch().arc((-90,-4),(-85,-13),(-89,-3)).arc((-89,-6),(-90,-4)).assemble().finalize().extrude(-115).union(w0.workplane(offset=-32/2).moveTo(24.5,-57).box(93,54,32)).union(w0.sketch().push([(-44,33)]).circle(20).push([(35,28)]).circle(56).finalize().extrude(85))