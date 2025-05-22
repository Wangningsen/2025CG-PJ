import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-48))
r=w0.sketch().push([(0,47)]).circle(53).rect(16,84,mode='s').push([(50,-87)]).rect(4,26).finalize().extrude(96)