import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,92))
w1=cq.Workplane('XY',origin=(0,0,50))
r=w0.sketch().push([(12,-67)]).circle(33).push([(8,-73)]).circle(3,mode='s').finalize().extrude(-13).union(w1.sketch().arc((-39,9),(-25,3),(-14,-6)).arc((29,92),(-39,9)).assemble().finalize().extrude(-142))