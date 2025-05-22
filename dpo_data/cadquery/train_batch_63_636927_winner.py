import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,15))
r=w0.sketch().segment((-38,5),(38,5)).arc((0,29),(-38,5)).assemble().finalize().extrude(-115).union(w0.sketch().push([(0,-12)]).circle(17).push([(11.5,-16.5)]).rect(5,3,mode='s').finalize().extrude(84)).union(w0.workplane(offset=85/2).moveTo(0,5.5).box(8,21,85))