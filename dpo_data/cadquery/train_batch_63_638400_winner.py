import cadquery as cq
w0=cq.Workplane('YZ',origin=(40,0,0))
w1=cq.Workplane('XY',origin=(0,0,-58))
r=w0.sketch().segment((-100,-19),(-30,-70)).segment((6,-21)).segment((6,-29)).segment((100,-29)).segment((100,70)).segment((6,70)).segment((6,35)).segment((-37,66)).close().assemble().finalize().extrude(-130).union(w1.sketch().push([(31.5,49.5)]).rect(117,31).push([(31.5,50)]).rect(19,20,mode='s').finalize().extrude(71))