import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,31))
r=w0.workplane(offset=-62/2).moveTo(22,-62).box(16,76,62).union(w0.sketch().push([(-57,65)]).circle(35).push([(-53,65)]).circle(13,mode='s').finalize().extrude(-7)).union(w0.sketch().push([(-26.5,-62)]).rect(27,70).push([(-26,-62)]).circle(7,mode='s').push([(65,-42)]).circle(27).finalize().extrude(-4))