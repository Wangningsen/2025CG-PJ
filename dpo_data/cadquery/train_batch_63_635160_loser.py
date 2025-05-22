import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,15))
r=w0.sketch().push([(-85,-8)]).circle(6).circle(2,mode='s').finalize().extrude(-115).union(w0.workplane(offset=-32/2).moveTo(24.5,-57).box(93,54,32)).union(w0.sketch().push([(-44,33)]).circle(20).push([(35,28)]).circle(56).finalize().extrude(85))