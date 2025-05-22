import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,0))
w1=cq.Workplane('XY',origin=(0,0,-15))
r=w0.sketch().push([(-10.5,-14.5)]).rect(75,63).push([(-4,-32.5)]).rect(12,9,mode='s').finalize().extrude(-100).union(w0.sketch().push([(-63,-14)]).rect(44,12).push([(-63.5,-14)]).rect(7,2,mode='s').finalize().extrude(28)).union(w1.workplane(offset=115/2).moveTo(23,26.5).box(124,39,115))