import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-1))
r=w0.workplane(offset=-99/2).cylinder(99,19).union(w0.sketch().circle(56).push([(41,-6)]).circle(6,mode='s').finalize().extrude(101))