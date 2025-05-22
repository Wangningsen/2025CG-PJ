import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,15))
r=w0.sketch().segment((-38,5),(38,5)).arc((0,29),(-38,5)).assemble().finalize().extrude(-115).union(w0.sketch().push([(0,-12)]).circle(17).push([(11,-15)]).circle(2,mode='s').finalize().extrude(84)).union(w0.workplane(offset=85/2).moveTo(0,6.5).box(8,19,85))